import json
import requests

params_search="search?artistOrCulture=true&q="

params_objectID="objects/"

params_word="search?q="


while True:
    
    search_type=input ("how would you like to search piece of art: \n  A) by Artist or Culture.  \t B)by any word related" + "\n [A or B]/[Artist,Culture or Word:    ")

    option1="A"
    option1_artist="Artist"
    option1_artist2="Culture"
    option2="B"
    option2_word="Word"

    if (search_type.lower()==option1.lower()) or (search_type.lower()==option1_artist.lower()) or (search_type.lower()==option1_artist2.lower()):

        artistName=input("Enter Artist Name or Culture or Nationality: ")

        URL_search=f"https://collectionapi.metmuseum.org/public/collection/v1/{params_search}{artistName}"
        r=requests.get(url=URL_search)

        data_json=r.json()

        data_str=json.dumps(data_json, indent=2) #printing the Json in a organized way

        print(data_str)

        idNumber=input("enter any id(from Above) to check the piece of art: ")

        URL_objectID=f"https://collectionapi.metmuseum.org/public/collection/v1/{params_objectID}{idNumber}"
        r=requests.get(url=URL_objectID)

        objectData=r.json()

        objectStr=json.dumps(objectData, indent=2)

        print(objectStr)

    elif(search_type.lower()==option2.lower()) or (search_type.lower()==option2_word.lower()):

        word_related=input("enter any word: ")
        URL_word=f"https://collectionapi.metmuseum.org/public/collection/v1/{params_word}{word_related}"
        r=requests.get(url=URL_word)

        word_json=r.json()

        word_str=json.dumps(word_json, indent=2)

        print(word_str)

        idNumber=input("enter any id(from Above) to check the piece of art: ")

        URL_objectID=f"https://collectionapi.metmuseum.org/public/collection/v1/{params_objectID}{idNumber}"
        r=requests.get(url=URL_objectID)

        objectData=r.json()

        objectStr=json.dumps(objectData, indent=2)

        print(objectStr)

    else:
        print("not a choice")
    
    break
    



