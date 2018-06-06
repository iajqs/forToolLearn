import jieba
import re
jieba.load_userdict('../Jieba/dict.txt')
# first,
# # if the label is 0, we let the src add susp as one sentence
# # if the label is 1, we let the src and susp as two sentence
def generateLableSentence(inpath, outpath):
    with open(inpath, 'r', encoding='utf-8') as fin, open(outpath, 'w', encoding='utf-8') as fout:
        for line in fin:
            _, sen1, sen2, label = line.strip().split('\t')
            sen1 = re.sub('[﻿ ,.!，。！？?]','',sen1)
            sen2 = re.sub('[﻿ ,.!，。！？?]','',sen2)
            ### seg
            words1= [ w for w in jieba.cut(sen1) if w.strip() ]
            words2= [ w for w in jieba.cut(sen2) if w.strip() ]
            ### if label is 1, connect
            if label == '1':
                fout.write(' '.join(words1) + '\n')
                fout.write(' '.join(words2) + '\n')
            ### if label is 0, distribute
            if label == '0':
                fout.write(' '.join(words1) + ' ' + ' '.join(words2) + '\n')

# second,
# # src as one sentence, susp as one sentence
def generateOriSentence(inpath, outpath):
    with open(inpath, 'r', encoding='utf-8') as fin, open(outpath, 'w', encoding='utf-8') as fout:
        for line in fin:
            _, sen1, sen2, label = line.strip().split('\t')
            sen1 = re.sub('[﻿ ,.!，。！？?]','',sen1)
            sen2 = re.sub('[﻿ ,.!，。！？?]','',sen2)
            ### seg
            words1= [ w for w in jieba.cut(sen1) if w.strip() ]
            words2= [ w for w in jieba.cut(sen2) if w.strip() ]
            fout.write(' '.join(words1) + '\n')
            fout.write(' '.join(words2) + '\n')

inPath = 'E:\\学习资料\\自然语言处理\\forToolLearn\\data\\ATEC\\Origin\\atec_nlp_sim_train_all.csv'
outLabelPath = 'E:\\学习资料\\自然语言处理\\forToolLearn\\data\\ATEC\\gensim\\labelSentences.txt'
outPath = 'E:\\学习资料\\自然语言处理\\forToolLearn\\data\\ATEC\\gensim\\Sentences.txt'
generateLableSentence(inPath, outLabelPath)
generateOriSentence(inPath, outPath)