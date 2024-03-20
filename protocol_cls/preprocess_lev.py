# -*- coding: utf-8 -*-
# @Author: xiegr
# @Date:   2020-08-28 21:26:15
# @Last Modified by:   xiegr
# @Last Modified time: 2020-09-16 21:19:38

import dpkt
import pickle
import os

protocols = ['dns', 'smtp', 'ssh', 'ftp', 'http', 'https']
ports = [53, 25, 22, 21, 80, 443]
xgr = 0

def gen_flows(pcap):
	flows = [{} for _ in range(len(protocols))]

	if pcap.datalink() != dpkt.pcap.DLT_EN10MB:
		print('unknow data link!')
		return

	
	for _, buff in pcap:
		eth = dpkt.ethernet.Ethernet(buff)
		xgr += 1
		if xgr % 500000 == 0:
			print('The %dth pkt!'%xgr)
			# break

		if isinstance(eth.data, dpkt.ip.IP) and (
		isinstance(eth.data.data, dpkt.udp.UDP)
		or isinstance(eth.data.data, dpkt.tcp.TCP)):
			# tcp or udp packet
			ip = eth.data

			# loop all protocols
			for name in protocols:
				index = protocols.index(name)
				if ip.data.sport == ports[index] or \
				ip.data.dport == ports[index]:
					if len(flows[index]) >= 10000:
						# each class has at most 1w flows
						break
					# match a protocol
					key = '.'.join(map(str, map(int, ip.src))) + \
					'.' + '.'.join(map(str, map(int, ip.dst))) + \
					'.' + '.'.join(map(str, [ip.p, ip.data.sport, ip.data.dport]))

					if key not in flows[index]:
						flows[index][key] = [ip]
					elif len(flows[index][key]) < 1000:
						# each flow has at most 1k flows
						flows[index][key].append(ip)
					# after match a protocol quit
					break

	return flows




def closure(flows):
	flow_dict = {}
	for name in protocols:
		index = protocols.index(name)
		flow_dict[name] = flows[index]
		print('============================')
		print('Generate flows for %s'%name)
		print('Total flows: ', len(flows[index]))
		cnt = 0
		for k, v in flows[index].items():
			cnt += len(v)
		print('Total pkts: ', cnt)

	with open('pro_flows.pkl', 'wb') as f:
		pickle.dump(flow_dict, f)

if __name__ == '__main__':
	#pcap = dpkt.pcap.Reader(open('/data/xgr/sketch_data/wide/202006101400.pcap', 'rb'))
	pcap_data_dir = 'e:/data_mining/cyber/mini_project/data_unibs_new/'
	pcap_list = os.listdir(pcap_data_dir)
	pcap_list = [pcap_data_dir+f for f in pcap_list if f.endswith('.pcap')]
	all_flows_dict = []
	for pcap_file in pcap_list:
		pcap = dpkt.pcap.Reader(open(pcap_file, 'rb'))
		flows = gen_flows(pcap)
		all_flows_dict.extend(flows)
	closure(all_flows_dict)


