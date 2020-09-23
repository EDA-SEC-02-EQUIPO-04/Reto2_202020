"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me

assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria.
"""


# -----------------------------------------------------
# API del TAD Catalogo de películas.
# -----------------------------------------------------
def new_catalog():
    """ Inicializa el catálogo de películas

    Crea una lista vacia para guardar todas las películas.

    Se crean indices (Maps) por los siguientes criterios:
    id películas

    Retorna el catálogo inicializado.
    """
    catalog = {
        'details': lt.newList('SINGLE_LINKED'),
        'casting': lt.newList('SINGLE_LINKED'),
        # 'producer_companies': mp.newMap(1000, maptype='PROBING', loadfactor=2, comparefunction=compare_ids)
        # 'producer_companies': mp.newMap(200, maptype='PROBING', loadfactor=10, comparefunction=compare_ids)
        # 'producer_companies': mp.newMap(4000, maptype='PROBING', loadfactor=0.5, comparefunction=compare_ids)
        'movies_ids': mp.newMap(5000, maptype='PROBING', loadfactor=0.4, comparefunction=compare_ids),
        'production_companies': mp.newMap(1000, maptype='PROBING', loadfactor=0.4, comparefunction=compare_producers),
        'directors':mp.newMap(1000, maptype='PROBING', loadfactor=0.4,comparefunction=compareDirectors),
        'production_countries': mp.newMap(1000, maptype='PROBING', loadfactor=0.4, comparefunction=compare_countries)
        'genres': mp.newMap(1000, maptype='PROBING', loadfactor=0.4, comparefunction=compare_genres)

    }
    return catalog


def new_producer(name):
    """
    Crea una nueva estructura para modelar las películas de una compañia de producción
    y su promedio de ratings
    """
    producer = {'name': name, 'movies': lt.newList('SINGLE_LINKED', compare_producers), 'average_rating': 0}
    return producer

def new_director(name):
    """Crea una nueva estructura para modelar las películas de un director y su promedio de rating

    Args:
        name (name): Nombre del director 
    Returns:
        dict: Diccionario del director con su nombre, sus películas y el promedio de las mismas. 
    """
    director = {'name': name,
                'total_movies':0,
                'movies': lt.newList('SINGLE_LINKED', compareDirectors),
                'average_rating': 0.0}
    return director

def new_producer_country(name):
    """Crea una nueva estructura para modelar las películas de un país productor de películas y su promedio de rating

    Args:
        name (name): Nombre del país de producción
    Returns:
        dict: Diccionario del país con su nombre, sus películas y el año. 
    """
    country = {'name': name,
               'movies': lt.newList('SINGLE_LINKED', compare_producers),
               'year': 0,
               'director': None}
    return country

def new_genre(name):
    """
    Crea una nueva estructura para modelar las películas de una compañia de producción
    y su promedio de ratings
    """
    genre = {'name': name, 'movies': lt.newList('SINGLE_LINKED', compare_producers), 'average_rating': 0}
    return genre


# Funciones para agregar información al catálogo.


def add_details(catalog, movie):
    """
    Esta función adiciona detalles a la lista de películas,
    adicionalmente los guarda en un Map usando como llave su id.
    """
    lt.addLast(catalog['details'], movie)
    mp.put(catalog['movies_ids'], movie['id'], movie)



def addDirector(catalog, director):
    """
    Adiciona un director al catalogo
    """
    lt.addLast(catalog['casting'], director)
    mp.put(catalog['directors'], director['id'], director)


def add_movie_production_companies(catalog, producer_name, movie):
    producers = catalog['production_companies']
    existproducer = mp.contains(producers, producer_name)
    if existproducer:
        entry = mp.get(producers, producer_name)
        producer = me.getValue(entry)
    else:
        producer = new_producer(producer_name)
        mp.put(producers, producer_name, producer)
    lt.addLast(producer['movies'], movie)
    # Producer vote average.
    producer_avg = producer['average_rating']
    movie_avg = movie['vote_average']
    if producer_avg == 0.0:
        producer['average_rating'] = float(movie_avg)
    else:
        producer['average_rating'] = (producer_avg + float(movie_avg)) / 2
 

def add_movie_production_countries(catalog, country, movie):
    producer_countries = catalog['production_countries']
    existproducer = mp.contains(producer_countries, country)
    if existproducer:
        entry = mp.get(producer_countries, country)
        producer = me.getValue(entry)
    else:
        producer = new_producer_country(country)
        mp.put(producer_countries, country, producer)
    lt.addLast(producer['movies'], movie)



def add_movie_genre(catalog, genre_name, movie):
    genres = catalog['genres']
    existgenre = mp.contains(genres, genre_name)
    if existgenre:
        entry = mp.get(genres, genre_name)
        genre = me.getValue(entry)
    else:
        genre = new_genre(genre_name)
        mp.put(genres, genre_name, genre)
    lt.addLast(genre['movies'], movie)
    # Genre vote average.
    genre_avg = genre['average_rating']
    movie_avg = movie['vote_average']
    if genre_avg == 0.0:
        genre['average_rating'] = float(movie_avg)
    else:
        genre['average_rating'] = (genre_avg + float(movie_avg)) / 2


# ==============================
# Funciones de consulta
# ==============================

def details_size(catalog):
    # Número de detalles en el catálogo.
    return lt.size(catalog['details'])


def casting_size(catalog):
    # Número de elencos en el catálogo.
    return lt.size(catalog['casting'])


def show_movie_data(catalog, index):
    el = lt.getElement(catalog['details'], index)
    return (f'- {el["title"]}:'
            + f'\n   con un puntaje promedio de {el["vote_average"]} y un total de {el["vote_count"]} votaciones,'
            + f'\n   fue estrenada en {el["release_date"]} en el idioma "{el["original_language"]}".')


def show_producer_data(producer):
    """
    Imprime las películas de una productara.
    """
    if producer:
        print(producer)
        print('Productora de cine encontrada: ' + producer['name'])
        print('Promedio: ' + str(producer['average_rating']))
        print('Total de películas: ' + str(lt.size(producer['movies'])))
        iterator = it.newIterator(producer['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print('Título: ' + movie['title'] + ' | Vote Average: ' + movie['vote_average'])
    else:
        print('No se encontró la productora')

def show_director_data(director):
    """
    Imprime las películas de un director.
    """
    if director:
        print(director)
        print('Director de cine encontrado: ' + director['name'])
        print('Promedio: ' + str(director['average_rating']))
        print('Total de películas: ' + str(lt.size(director['movies'])))
        iterator = it.newIterator(director['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print('Título: ' + movie['title'] + ' | Vote Average: ' + movie['vote_average'])
    else:
        print('No se encontró el director')

def show_producer_country(country):
    """
    Imprime las películas de una productara.
    """
    if country:
        print('País de producción de cine encontrada: ' + country['name'])
        print('Promedio: ' + str(country['average_rating']))
        print('Total de películas: ' + str(lt.size(country['movies'])))
        iterator = it.newIterator(country['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print('Título: ' + movie['title'] + ' | Relase Date: ' + movie['relase_date'])
    else:
        print('No se encontró el país')

def show_genre_data(genre):
    """
    - Imprime la lista de todas las películas asociadas a un género.
    - El total de películas.
    - El promedio de votos del género.
    """
    iterator = it.newIterator(genre['movies'])
    while it.hasNext(iterator):
        movie = it.next(iterator)
        print('Título: ' + movie['title'] + ' | Vote Average: ' + movie['vote_average'])
    print('\nGénero(s) de películas a buscar: ' + genre['name'])
    print('Promedio: ' + str(genre['average_rating']))
    print('Total de películas: ' + str(lt.size(genre['movies'])))
    print('---------------------')


def total_average(lista):
    total = lt.size(lista)
    votes = 0
    for i in range(lt.size(lista)):
        movie = lt.getElement(lista, i)
        votes += float(movie)
    total_vote_average = votes / total
    return round(total_vote_average, 1)


def get_movie_producer(catalog, producer_name):
    """
    Retorna las películas a partir del nombre de la productora
    """
    producer = mp.get(catalog['production_companies'], producer_name)
    if producer:
        return me.getValue(producer)
    return None

def get_director_movies(catalog, director_name):
    """
    Retorna la lista de películas asociadas a un director
    """
    director = mp.get(catalog['directors'], director_name)
    if director:
        return me.getValue(director)
    return None


def get_movie_country(catalog, countries):
    """
    Retorna las películas a partir del nombre de la productora
    """
    country = mp.get(catalog['production_countries'], countries)
    if country:
        return me.getValue(country)
    return None

            
def get_genre_movies(catalog, genre):
    """
    Retorna las películas a partir del nombre del género.
    """
    genre_movies = mp.get(catalog['genres'], genre)
    if genre_movies:
        return me.getValue(genre_movies)
    return None


def search_genres(catalog, genres):
    for index in range(len(genres)):
        genres[index] = genres[index].capitalize()
        existgenre = mp.contains(catalog['genres'], genres[index])
        if not existgenre:
            print('Un género no se encuentra. Intente de nuevo.')
            return None
    return genres


# ==============================
# Funciones de Comparacion
# ==============================
def compare_ids(id_, tag):
    entry = me.getKey(tag)
    if int(id_) == int(entry):
        return 0
    elif int(id_) > int(entry):
        return 1
    else:
        return 0


def compare_producers(keyname, producer):
    proentry = me.getKey(producer)
    if keyname == proentry:
        return 0
    elif keyname > proentry:
        return 1
    else:
        return -1

def compareDirectors(keyname, producer):
    dientry = me.getKey(producer)
    if keyname == dientry:
        return 0
    elif keyname > dientry:
        return 1
    else:
        return -1

def compare_countries(keyname, country):
    coentry = me.getKey(country)
    if keyname == coentry:
        return 0
    elif keyname > coentry:
        return 1
    else:
        return -1


def compare_genres(keyname, producer):
    proentry = me.getKey(producer)
    if keyname == proentry:
        return 0
    elif keyname > proentry:
        return 1
    else:
        return -1

