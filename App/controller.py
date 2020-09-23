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

import config as cf
from App import model
import csv
from time import process_time

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""


# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________
def init_catalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo.
    t1_start = process_time()  # tiempo inicial
    catalog = model.new_catalog()
    t1_stop = process_time()  # tiempo final
    print('Tiempo de ejecución ', t1_stop - t1_start, ' segundos')
    return catalog


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def load_data(catalog, casting_file, details_file):
    """
    Carga los datos de los archivos en el modelo
    """
    t1_start = process_time()  # tiempo inicial
    load_details(catalog, details_file)
    load_casting(catalog, casting_file)
    t1_stop = process_time()  # tiempo final
    print('Tiempo de ejecución ', t1_stop - t1_start, ' segundos')


def load_details(catalog, details_file):
    """
    Carga cada una de las lineas del archivo de detalles.
    - Se agrega cada película al catalogo de películas.
    - Por cada libro se encuentran sus autores y por cada
      autor, se crea una lista con sus libros
    """
    dialect, dialect.delimiter = csv.excel(), ';'
    with open(details_file, encoding='utf-8-sig') as input_file:
        file_reader = csv.DictReader(input_file, dialect=dialect)
        for movie in file_reader:
            strip_movie = {}
            for key, value in movie.items():
                strip_movie[key.strip()] = value.strip()
            movie = strip_movie
            model.add_details(catalog, movie)
            producer_names = movie['production_companies'].split(",")
            genres = movie['genres'].split(",")
            for producer in producer_names:
                model.add_movie_production_companies(catalog, producer, movie)
            for genre in genres:
                genre = genre.split('|')
                for subgenre in genre:
                    model.add_movie_genre(catalog, subgenre, movie)


def load_casting(catalog, casting_file):
    """
    Carga en el catalogo el elenco a partir de la información
    del archivo de casting.
    """
    dialect, dialect.delimiter = csv.excel(), ';'
    with open(casting_file, encoding='utf-8-sig') as input_file:
        file_reader = csv.DictReader(input_file, dialect=dialect)
        for movie in file_reader:
            strip_movie = {}
            for key, value in movie.items():
                strip_movie[key.strip()] = value.strip()
            movie = strip_movie
            model.add_casting(catalog, movie)


# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________
def details_size(catalog):
    # Numero de detallesleídos.
    return model.details_size(catalog)


def casting_size(catalog):
    # Numero de elencos leídos.
    return model.casting_size(catalog)


def show_movie(catalog, index):
    t1_start = process_time()  # tiempo inicial
    print(model.show_movie_data(catalog, index))
    t1_stop = process_time()  # tiempo final
    print('Tiempo de ejecución ', t1_stop - t1_start, ' segundos')


def production_companies(catalog, production):
    t1_start = process_time()  # tiempo inicial
    print('Las películas de la productora son: ')
    average, size = get_movies_by_producer(catalog, production)
    print('Tienen un promedio de ', average, ' y han producido ', size, ' películas')
    t1_stop = process_time()  # tiempo final
    print('Tiempo de ejecución ', t1_stop - t1_start, ' segundos')


def get_movies_by_producer(catalog, producer_name):
    """
     Retorna las películas de una productora.
    """
    producerinfo = model.get_movie_producer(catalog, producer_name)
    return producerinfo


def get_movies_by_genre(catalog, genre):
    """
     Retorna las películas de una productora.
    """
    genre_info = model.get_genre_movies(catalog, genre)
    return genre_info


def show_producer_data(producer):
    t1_start = process_time()  # tiempo inicial
    model.show_producer_data(producer)
    t1_stop = process_time()  # tiempo final
    print('Tiempo de ejecución ', t1_stop - t1_start, ' segundos')


def show_genre_data(genre_info):
    model.show_genre_data(genre_info)


def search_genres(catalog):
    genres = input('Ingrese el género. Si son varios, separe por comas: ')
    genres = genres.replace(' ', '')
    genres = genres.split(',')
    genres = model.search_genres(catalog, genres)
    if genres is None:
        return search_genres(catalog)
    return genres
