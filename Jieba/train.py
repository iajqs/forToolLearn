import jieba
import numpy as np

# get the origin data
def getTheOriginData(path):
    with open(path,encoding='UTF-8') as file_object:
        contents = file_object.read()
    ##split the data by line
    lines = contents.split('\n')
    ##the labels
    labels = []
    ##the pairslist which is store the pairs
    featureset = []
    ##get the pairs and the labels
    for line in lines:
        if len(line) == 0:
            continue
        strs = line.split('\t')

        labels.append(int(strs[0]))

        strs[1] = strs[1].replace('[','').replace(']','')
        numbers = strs[1].split(', ')
        features = []
        for number in numbers:
            features.append(float(number))
        featureset.append(features)
    return labels, featureset



##get the data
##get the train data
ori_trainPath = 'E:/学习资料/自然语言处理/forToolLearn/data/ATEC/data/jieba/atec_nlp_sim_train_all/posFeature4.txt'
train_labels, train_featureset = getTheOriginData(ori_trainPath)
ori_testPath = 'E:/学习资料/自然语言处理/forToolLearn/data/ATEC/data/jieba/atec_nlp_sim_train_all/posFeature.txt'
test_labels, test_featureset = getTheOriginData(ori_testPath)
from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,batch_size=128,
                   hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(train_featureset, train_labels)
y_pred = clf.predict(test_featureset)
y_true = test_labels

for i in range(len(y_pred)):
    pred = y_pred[i]
    true = y_true[i]
    if pred == true and pred == 1:
        print(i)

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
print('accuracy',accuracy_score(y_true, y_pred))
print('precision',precision_score(y_true, y_pred))
print('f1',f1_score(y_true, y_pred))
print('recall',recall_score(y_true, y_pred))