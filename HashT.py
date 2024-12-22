import re

pattern = r"#\w+"

file = 'fichier.txt'
with open(file, 'r', encoding='utf-8') as fichier:
    contenu = fichier.read()

hashtags = re.findall(pattern, contenu)

if hashtags:
    print("the hashtags :")
    for hashtag in hashtags:
        print(hashtag)
        file = 'final.txt'
        with open(file, "a+", encoding='utf-8') as filee:
            filee.write(hashtag + "\n")

else:
    print("Aucun hashtag trouvé dans le fichier.")
