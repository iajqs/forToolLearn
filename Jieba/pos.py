import jieba
import jieba.posseg as pseg

jieba.load_userdict('./dict.txt')

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

# seg and pos the word by jieba
def seg(pairslists):
    segLists = []
    for pairslist in pairslists:
        segList = []
        src = pairslist[0]
        susp = pairslist[1]
        segList.append(pseg.cut(src))
        segList.append(pseg.cut(susp))
        segLists.append(segList)
    return segLists



##get the data
##get the train data
ori_trainPath = 'E:/学习资料/自然语言处理/forToolLearn/data/ATEC/Origin/atec_nlp_sim_train.csv'
train_labels, train_pairslist = getTheOriginData(ori_trainPath)


segLists = seg(train_pairslist)
with open('E:/学习资料/自然语言处理/forToolLearn/data/ATEC/data/pos.txt', 'w',encoding='UTF-8') as fs:
    for i in range(len(segLists)):
        segList = segLists[i]
        label = train_labels[i]
        src = segList[0]
        susp = segList[1]
        srcstr = ''
        suspstr = ''
        for word, flag in src:
            srcstr = srcstr + word+'/'+flag+' '
        for word, flag in susp:
            suspstr = srcstr + word + '/' + flag + ' '
        fs.write(label+'\t'+srcstr+'\t'+suspstr+'\n')
