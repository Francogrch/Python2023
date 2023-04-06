import json
import csv
import collections

with open("netflix_titles.csv") as peliculas: 
    csv_list = list(csv.DictReader(peliculas))
    #Guardo las peliculas que tienen mas de un pais, creo y cargo el JSON
    list_films = [film for film in csv_list if ", " in film["country"]]
    films_more_one_country = open("filmsMoreOneCountry.json","w")
    json.dump(list_films,films_more_one_country)
    films_more_one_country.close()

    #Armo lista con los paises de las peliculas
    list_country = [] #Intente hacerlo por comprension y la verdad no pude
    for films in csv_list:
        for country in films['country'].split(', '):
            if country != '':
                list_country.append(country)
    
    tuple_counter = tuple((collections.Counter(list_country)).most_common())
    print(f"""Los 5 paises con mas producciones son:
    1.{tuple_counter[0][0]} con {tuple_counter[0][1]} peliculas.
    2.{tuple_counter[1][0]} con {tuple_counter[1][1]} peliculas.
    3.{tuple_counter[2][0]} con {tuple_counter[2][1]} peliculas.
    4.{tuple_counter[3][0]} con {tuple_counter[3][1]} peliculas.
    5.{tuple_counter[4][0]} con {tuple_counter[4][1]} peliculas.
    """)
    
