import random
import json
import pickle
import numpy as np
import tensorflow as tf
import pywhatkit as pwk
import requests
import os 
from googletrans import Translator

import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import load_model

lemmantizer = WordNetLemmatizer()

translator = Translator()
translator.translate('Hola, como estás ?')
intents = json.loads(open('intents.json', encoding='utf-8').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))    

model = load_model('chatbot_simplemodel.h5')

def tradutor (Frase_traduzida):
    try:
        Resposta = translator.translate(Frase_traduzida, dest ="es")
        return Resposta.text
    except Exception as e:
           return "Internet pode estar ruim"

def cleanUpSentence(sentence):
    sentenceWords = nltk.word_tokenize(sentence)
    sentenceWords = [lemmantizer.lemmatize(word) for word in sentenceWords]
    return sentenceWords    

def bagOfWords(sentence):
    sentenceWords = cleanUpSentence(sentence)
    bag = [0] * len(words)
    for w in sentenceWords:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predictClass(sentence):
    bow = bagOfWords(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    returnList = []
    for r in results:
        returnList.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return returnList

def getResponse(intentsList, intentsJson):
    tag = intentsList[0]['intent']
    listOfIntents = intentsJson['intents']
    for i in listOfIntents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

def buscar_dolar():
    try: 
        url = "https://economia.awesomeapi.com.br/last/USD-BRL"
        res = requests.get(url)
        dados = res.json()
        # Convertemos para float para o :.2f funcionar
        valor = float(dados['USDBRL']["bid"]) 
        return f"O dólar está saindo a R$ {valor:.2f} agora."
    except Exception as e:
        # Dica: imprimir o erro 'e' ajuda a saber se o site caiu ou se é erro no código
        return "Ta pobre ein filho, não consegui nem ver a cotação."
 
print("Go! Bot is running!")

while True:
    message = input("Você: ")
    if message.lower() in ["sair", "parar", "quit"]:
        break

    ints = predictClass(message)

    if len(ints) > 0:
        tag = ints[0]['intent']
        
        if tag == "cotacao_dolar":
            res = buscar_dolar()
            print(f"Bot: {res}")

        elif tag == "traducao":
            res_json = getResponse(ints, intents)
            print(f"Bot: {res_json}")
            frase_para_processar = input("Sua frase: ")
            resultado =tradutor(frase_para_processar)
            print(f"Bot: A tradução é: {resultado}")
            continue 

        else:
            res3 = "Não entendi, pode repetir?"
            print(f"Bot: {res3}")
    else:
        print("Não entendi, pode repetir? ")
