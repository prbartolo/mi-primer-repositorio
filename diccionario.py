meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print("significa:", {meme_dict[word]})
else:
    print("Lo siento, esa palabra no esta en el diccionario") 
print(meme_dict["CRINGE"])
