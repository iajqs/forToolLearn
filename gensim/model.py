from gensim.models.word2vec import Word2Vec
import gensim

# generate the word2vec model
def generateModel(inPath,modelPath):
    sentences = []
    # get the train data
    with open(inPath, 'r', encoding='utf-8') as fin:
        for line in fin:
            sentence = line.split()
            if sentence.__contains__('得知'):
                print('yes')
            sentences.append(sentence)
    # train the model
    ## set the min count as 1
    model = Word2Vec(min_count=1)
    ## create the vocabulary
    model.build_vocab(sentences)
    ## train
    model.train(sentences, total_examples = model.corpus_count, epochs = model.iter)
    ## save the model
    model.save(modelPath)


inPathLabel = 'E:\\学习资料\\自然语言处理\\forToolLearn\\data\\ATEC\\gensim\\labelSentences.txt'
modelPathLabel = '/tmp/mymodel_label'
inPath = 'E:\\学习资料\\自然语言处理\\forToolLearn\\data\\ATEC\\gensim\\Sentences.txt'
modelPath = '/tmp/mymodel'
generateModel(inPathLabel, modelPathLabel)
generateModel(inPath, modelPath)
model = gensim.models.Word2Vec.load(modelPath)
print(model['得知'])