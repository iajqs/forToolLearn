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

# get the Featureset by posed word
def getFeature(src, susp):

    ## delete the space which is in begin or end
    src = src.strip()
    susp = susp.strip()

    ## split by space
    src_items = src.split(' ')
    susp_items = susp.split(' ')

    ## init a featureindex <feature, index>
    features = {}
    ## init the feature items
    items = ['r', 'd', 'v', 'nz', 'u', 'n', 'f', 'w', 't', 'y', 'ad', 'vn', 'm', 'p', 'a', 'j', 'b', 'an', 'q', 'c', 's', 'Ng', 'i', 'nr', 'Tg', 'Vg', 'j', 'l', 'nx', 'z', 'vd', 'n]', 'Ag', 'ns', 'k', 'Mg', 'o', 'Bg', 'nt', 'Dg', 'h', 'e']
    ## init the index
    index = 0
    ## init the Matrix of featureset
    ### for example 'r' is save the item from src which is the same with the item from susp and the pos is 'r',
            #### we add 1 to the featuresMatrix[features['r']]
    ### for example '_r' is save the  item from src and susp which can't find the same item from susp and the pos is 'r',
            #### we add 1 to the featuresMatrix[features['_r']]
    ### for susp , the 'r' change to 'pr', '_r' change to '_pr' (I think this could have a chance)
    featuresMatrix = []
    import numpy as np
    countItem = {}
    for i in range(len(items)*2):
        featuresMatrix.append(0)
    for item in items:
        features[item] = index
        index += 1
        features['_'+item] = index
        index += 1
        countItem[item] = 0
    # count the number of all pos
    for src_item in src_items:
        src_tag = src_item.split('/')[1]
        if not (features.__contains__(src_tag)):
            continue
        countItem[src_tag] += 1
    for susp_item in susp_items:
        susp_tag = susp_item.split('/')[1]
        if not (features.__contains__(susp_tag)):
            continue
        countItem[susp_tag] += 1

    for src_item in src_items:
        src_word = src_item.split('/')[0]
        src_tag = src_item.split('/')[1]
        if not (features.__contains__(src_tag)):
            continue
        index = features[src_tag]
        sign = 1
        for susp_item in susp_items:
            susp_word = susp_item.split('/')[0]
            susp_tag = susp_item.split('/')[1]
            if src_item == susp_item:
                featuresMatrix[index] += 1
                sign = 0
                break
        featuresMatrix[index+1] += sign

    for src_item in susp_items:
        src_word = src_item.split('/')[0]
        src_tag = src_item.split('/')[1]
        if not (features.__contains__(src_tag)):
            continue
        index = features[src_tag]
        sign = 1
        for susp_item in src_items:
            susp_word = susp_item.split('/')[0]
            susp_tag = susp_item.split('/')[1]
            if src_item == susp_item:
                featuresMatrix[index] += 1
                sign = 0
                break
        featuresMatrix[index+1] += sign

    for item in items:
        index = features[item]
        if countItem[item] == 0:
            continue
        featuresMatrix[index] /= countItem[item]
        featuresMatrix[index+1] /= countItem[item]
    return featuresMatrix


##get the data
##get the train data
ori_trainPath = 'E:/学习资料/自然语言处理/forToolLearn/data/ATEC/Origin/atec_nlp_sim_train_all.csv'
train_labels, train_pairslist = getTheOriginData(ori_trainPath)


segLists = seg(train_pairslist)
sign = 1
########
# posFeature.txt the Standard Featureset 1 x label(1), 1 x label(0)
# posFeature4.txt 4 x label(1),1 x label(0)
# posFeature0.25.txt 1 x label(1). 0.25 x label(0)
########
with open('E:/学习资料/自然语言处理/forToolLearn/data/ATEC/data/jieba/atec_nlp_sim_train_all/posFeature.txt', 'w',encoding='UTF-8') as fs:
    for i in range(len(segLists)):
        segList = segLists[i]
        label = train_labels[i]
        src = segList[0]
        susp = segList[1]
        srcstr = ''
        suspstr = ''
        for word, flag in src:
            if word == '/':
                continue
            srcstr = srcstr + word+'/'+flag+' '
        for word, flag in susp:
            if word == '/':
                continue
            suspstr = srcstr + word + '/' + flag + ' '
        fs.write(label + '\t' + str(getFeature(srcstr, suspstr)) + '\n')
        # 4
        # if label == '0':
        #     fs.write(label + '\t' + str(getFeature(srcstr, suspstr)) + '\n')
        # else:
        #     for j in range(4):
        #         fs.write(label + '\t' + str(getFeature(srcstr, suspstr)) + '\n')
