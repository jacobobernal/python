meme_dict = {
    "facto" : "algo que es verdad",
    "parchao" : "relajado"
}

word = input("escriba la palabra que no entienda (¡¡Todo en minusculas por favor!!")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print ("la palabra no existe")
