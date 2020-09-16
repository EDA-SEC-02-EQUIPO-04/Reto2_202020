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
from DISClib.DataStructures import chaininghashtable as cht
from DISClib.DataStructures import probehashtable as pht

assert config

"""
  Este módulo implementa el tipo abstracto de datos
  (TAD) Map sin orden. Se puede implementar sobre una estructura
  de datos Hash Table, con resolución de colisiones: Linear Probing
  o separate chaining
"""


def newMap(numelements=17,
           prime=109345121,
           maptype='CHAINING',
           loadfactor=0.5,
           comparefunction=None):
    """Crea una tabla de simbolos (map) sin orden
    Args:
        numelements: Tamaño inicial de la tabla
        prime: Número primo utilizado en la función MAD
        maptype: separate chaining ('CHAINING' ) o linear probing('PROBING')
        loadfactor: Factor de carga inicial de la tabla
        comparefunction: Funcion de comparación entre llaves
    Returns:
        Un nuevo map
    Raises:
        Exception
    """
    if (maptype == 'CHAINING'):
        return cht.newMap(numelements,
                          prime,
                          loadfactor,
                          comparefunction)
    else:
        return pht.newMap(numelements,
                          prime,
                          loadfactor,
                          comparefunction)


def put(map, key, value):
    """ Ingresa una pareja llave,valor a la tabla de hash.
    Si la llave ya existe en la tabla, se reemplaza el valor

    Args:
        map: El map a donde se guarda la pareja
        key: la llave asociada a la pareja
        value: el valor asociado a la pareja
    Returns:
        El map
    Raises:
        Exception
    """
    if (map['type'] == 'CHAINING'):
        return cht.put(map, key, value)
    else:
        return pht.put(map, key, value)


def get(map, key):
    """ Retorna la pareja llave, valor, cuya llave sea igual a key
    Args:
        map: El map a donde se guarda la pareja
        key: la llave asociada a la pareja

    Returns:
        Una pareja <llave,valor>
    Raises:
        Exception
    """
    if (map['type'] == 'CHAINING'):
        return cht.get(map, key)
    else:
        return pht.get(map, key)


def remove(map, key):
    """ Elimina la pareja llave,valor, donde llave == key.
    Args:
        map: El map a donde se guarda la pareja
        key: la llave asociada a la pareja

    Returns:
        El map
    Raises:
        Exception
    """
    if (map['type'] == 'CHAINING'):
        return cht.remove(map, key)
    else:
        return pht.remove(map, key)


def contains(map, key):
    """ Retorna True si la llave key se encuentra en el map
        o False en caso contrario.
    Args:
        map: El map a donde se guarda la pareja
        key: la llave asociada a la pareja

    Returns:
        True / False
    Raises:
        Exception
    """
    if (map['type'] == 'CHAINING'):
        return cht.contains(map, key)
    else:
        return pht.contains(map, key)


def size(map):
    """  Retorna el número de entradas en la tabla de hash.
    Args:
        map: El map
    Returns:
        Tamaño del map
    Raises:
        Exception
    """
    if (map['type'] == 'CHAINING'):
        return cht.size(map)
    else:
        return pht.size(map)


def isEmpty(map):
    """ Informa si la tabla de hash se encuentra vacia
    Args:
        map: El map
    Returns:
        True: El map esta vacio
        False: El map no esta vacio
    Raises:
        Exception
    """
    if (map['type'] == 'CHAINING'):
        return cht.isEmpty(map)
    else:
        return pht.isEmpty(map)


def keySet(map):
    """
    Retorna una lista con todas las llaves de la tabla de hash

    Args:
        map: El map
    Returns:
        lista de llaves
    Raises:
        Exception
    """
    if (map['type'] == 'CHAINING'):
        return cht.keySet(map)
    else:
        return pht.keySet(map)


def valueSet(map):
    """
    Retorna una lista con todos los valores de la tabla de hash

    Args:
        map: El map
    Returns:
        lista de valores
    Raises:
        Exception
    """
    if (map['type'] == 'CHAINING'):
        return cht.valueSet(map)
    else:
        return pht.valueSet(map)
