#/usr/bin/env python
#coding=utf-8
import jieba
import sys

jieba.load_userdict('../Jieba/dict.txt')
def process(inpath):
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    with open(inpath, 'r', encoding='utf-8') as fin:
        for line in fin:
            lineno, sen1, sen2, label = line.strip().split('\t')
            words1= [ w for w in jieba.cut(sen1) if w.strip() ]
            words2= [ w for w in jieba.cut(sen2) if w.strip() ]
            union = words1 + words2
            same_num = 0
            for w in union:
                if w in words1 and w in words2:
                    same_num += 1
            if same_num * 2 >= len(union):
                if label == '1':
                    TP += 1
                elif label == '0':
                    FP += 1
            else:
                if label == '1':
                    FN += 1
                elif label == '0':
                    TN += 1
    return TP, TN, FP, FN
inpath = 'E:\\学习资料\\自然语言处理\\forToolLearn\\data\\ATEC\\Origin\\atec_nlp_sim_train_all.csv'
TP, TN, FP, FN = process(inpath)
precision = TP/(TP+FP)
recall = TP/(TP+FN)
f1 = (2*precision*recall)/(precision+recall)
print(TP, TN, FP, FN )

print('precision = ', precision)
print('recall = ', recall)
print('f1 = ', f1)