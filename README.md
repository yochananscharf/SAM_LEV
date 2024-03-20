# SAM-for-Traffic-Classification

Paper title: Self-attentive deep learning method for online traffic classification and its
interpretability

Accepted by Elsevier Computer Networks (https://doi.org/10.1016/j.comnet.2021.108267)  

More information about us https://xgr19.github.io

NetAI20 version https://github.com/xgr19/SAM-for-Traffic-Classification/tree/SAM-before-NetAI

**Run the files as follow:**

1. python3 preprocess_lev.py # reads in a `.pcap` file or a list of `.pcap` files and converts to `.pkl` file
2. python3 tool_lev.py # loads the pkl and converts to n pkl files for n-fold cross-validation
3. python3 train_lev.py # trains on n-fold cross-validation test-train datasets.

The dataset is available at http://mawi.wide.ad.jp/mawi/samplepoint-G/2020/202006101400.html

## Changes for the Cyber course

Copied all file in order to enable easier comparison (before/after). All the new files have `lev` appended to the file-name.

The changes are mainly in the `Network parameters` in lines `77-102` of `SAM_LEV.py`

Additionally all mention of the `y-input` which refers to `positional-encoding`, was removed in three files (`tool_lev.py`, `train_lev.py` and `SAM_LEV.py`).

This postional encoding is instead part of the network class instance. This saves resources by creating a sinlgle instance of a tensor representing the postional encoding and placing it on the device-memory (`GPU`).

Added code for counting the number of `parameters` in models.

![comparison of model parameters and embeddings](/SAM_diff.png)

