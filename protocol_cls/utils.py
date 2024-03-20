import pickle

import matplotlib.pyplot as plt
import seaborn as sns

#def show_confusion(pkl_path="results/cm_0.pkl" ):
pkl_path="E:/data_mining/cyber/mini_project/SAM-for-Traffic-Classification/results_lev/cm_0.pkl"
with open(pkl_path,'rb') as f:
	confusion_data = pickle.load(f)
print(confusion_data)
sns.heatmap(confusion_data.round(2), annot=True, fmt='g')
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.title('Confusion Matrix')
plt.show()