#coding: utf8
import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3


visual_recognition = VisualRecognitionV3('2016-05-20',api_key='800d6534163db6848332730ba6de9e45db7c0936')

# Exemplo de como abrir arquivos localmente
with open(join(dirname(__file__), 'C:/Users/david/Desktop/Visual Recognition/coca_latinha.jpg'), 'rb') as image_file:
	results = visual_recognition.classify(images_file=image_file)



with open(join(dirname(__file__), 'C:/Users/david/Desktop/Visual Recognition/coca.jpg'), 'rb') as image_file:
	results2 = visual_recognition.classify(images_file=image_file)

print("Resultados de reconhecimento de latinha de Coca-cola:\n")
print(json.dumps(results, indent=2))
print("Resultados de reconhecimento de garrafa de Coca-cola:\n")
print(json.dumps(results2, indent=2))


#Exemplo de como abrir arquivos por URL
print("Resultados de deteccao de faces:\n")
print(json.dumps(visual_recognition.detect_faces(images_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Official_portrait_of_Barack_Obama.jpg/440px-Official_portrait_of_Barack_Obama.jpg'), indent=2))    

#Exemplos para testes aleatórios
#https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Dilma_Rousseff_-_foto_oficial_2011-01-09.jpg/399px-Dilma_Rousseff_-_foto_oficial_2011-01-09.jpg
#https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Official_portrait_of_Barack_Obama.jpg/440px-Official_portrait_of_Barack_Obama.jpg
#https://upload.wikimedia.org/wikipedia/commons/d/d2/Donald_Trump_August_19%2C_2015_%28cropped%29.jpg



