import gensim
from gensim.models.word2vec import Word2Vec

def testModel(inPath,modelPath):
    model = gensim.models.Word2Vec.load(modelPath)
    sentences = []
    with open(inPath, 'r', encoding='utf-8') as fin:
        for line in fin:
            sentence = line.split()
            sentences.append(sentence)

    for i in range(10):
        sentence1 = sentences[i]
        i += 1
        sentence2 = sentences[i]
        print(model.n_similarity(sentence1, sentence2))



inPath = 'E:\\学习资料\\自然语言处理\\forToolLearn\\data\\ATEC\\gensim\\Sentences.txt'
modelPathLabel = '/tmp/mymodel_label'
modelPath = '/tmp/mymodel'
testModel(inPath, modelPathLabel)
print('-------------------------------------')
testModel(inPath, modelPath)
