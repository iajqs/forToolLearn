#/usr/bin/env python
#coding=utf-8
import jieba
import sys

jieba.load_userdict('../Jieba/dict.txt')
#Fillter, if the pair's sim bigger than 0.5, we Retain it
def process(inpath, outpath):
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
            if(sim >= 5):
                fout.write(line)

inpath = 'E:\\学习资料\\自然语言处理\\forToolLearn\\data\\ATEC\\Origin\\atec_nlp_sim_train_all.csv'
outpath = 'E:\\学习资料\\自然语言处理\\forToolLearn\\data\\ATEC\\Filter\\sim.csv'
process(inpath,outpath)