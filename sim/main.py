#/usr/bin/env python
#coding=utf-8
import jieba
import sys

jieba.load_userdict('../Jieba/dict.txt')
#Statistics, the relationship between the similarity distribution of each sentence pair and its corresponding tag.
def process(inpath, outpath):
    # The total number of 0, 1 labels in the training center
    sum0 = 0
    sum1 = 0
    # The number of the similarity in each interval
    section0 = {}
    section1 = {}
    with open(inpath, 'r', encoding='utf-8') as fin, open(outpath, 'w', encoding='utf-8') as fout:
        for line in fin:
            if len(line) == 0:
                continue
            # print(line)
            lineno, sen1, sen2, label = line.strip().split('\t')
            words1= [ w for w in jieba.cut(sen1) if w.strip() ]
            words2= [ w for w in jieba.cut(sen2) if w.strip() ]
            union = words1 + words2
            same_num = 0

            for w in union:
                if w in words1 and w in words2:
                    same_num += 1
            sim = int(same_num/len(union)*10)
            #If the tag is 0, update the corresponding number of corresponding labels in the 0 group.
            if not section0.__contains__(sim) and label =='0':
                sum0 += 1
                section0[sim] = 1
            elif label =='0':
                sum0 += 1
                section0[sim] += 1
            # If the tag is 1, update the corresponding number of corresponding labels in the 1 group.
            if not section1.__contains__(sim) and label =='1':
                sum1 += 1
                section1[sim] = 1
            elif label =='1':
                sum1 += 1
                section1[sim] += 1
        # the Proportion from 0 to i
        allPro0 = 0.0
        allPro1 = 0.0
        for i in range(10):
            number0 = section0[i]
            number1 = section1[i]
            p0 = number0/sum0
            p1 = number1/sum1
            allPro0 += p0
            allPro1 += p1
            fout.write(str(i)
                       +'\t'+ str(number0) +'\t'+ str(number1)
                       +'\t'+ str(p0) +'\t'+ str(p1)
                       +'\t'+ str(allPro0) +'\t'+ str(allPro1) + '\n')
        fout.write('0/1\t' + str(sum0) + '\t' + str(sum1) + '\t'  + '\n')
inpath = 'E:\\学习资料\\自然语言处理\\forToolLearn\\data\\ATEC\Origin\\atec_nlp_sim_train_all.csv'
outpath = 'E:\\学习资料\\自然语言处理\\forToolLearn\\data\\ATEC\\static\\simSection.txt'
process(inpath,outpath)