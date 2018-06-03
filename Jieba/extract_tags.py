import jieba
import jieba.analyse
from optparse import OptionParser

USAGE = "usage:    python extract_tags.py [file name] -k [top k]"

parser = OptionParser(USAGE)
parser.add_option("-k", dest="topK")
opt, args = parser.parse_args()

if opt.topK is None:
    topK = 10
else:
    topK = int(opt.topK)





# get the origin data
def getTheOriginData(path):
    with open(path,encoding='UTF-8') as file_object:
        contents = file_object.read()
    ##split the data by line
    lines = contents.split('\n')
    ##the labels
    labels = []
    ##the pairslist which is store the pairs
    pairslist = []
    ##get the pairs and the labels
    for line in lines:
        if len(line) == 0:
            continue
        line = line.replace(' ', '').replace('﻿','')
        pairs = []
        strs = line.split('\t')
        labels.append(strs[3])
        pairs.append(strs[1])
        pairs.append(strs[2])
        pairslist.append(pairs)

    return labels, pairslist

##get the data
##get the train data
ori_trainPath = 'E:/学习资料/自然语言处理/forToolLearn/data/ATEC/Origin/atec_nlp_sim_train_all.csv'
train_labels, train_pairslist = getTheOriginData(ori_trainPath)

y_pred = []
y_true = []

count = 0
count0 = 0
count1 = 0

tag0 = 0
tag1 = 0
for i in range(len(train_pairslist)):
    pairs = train_pairslist[i]
    label = train_labels[i]
    src = pairs[0]
    susp = pairs[1]
    srcTags = jieba.analyse.extract_tags(src, topK=topK)
    suspTags = jieba.analyse.extract_tags(susp, topK=topK)
    print(srcTags,suspTags)