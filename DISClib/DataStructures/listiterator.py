"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
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

from DISClib.DataStructures import arraylistiterator as ait
from DISClib.DataStructures import linkedlistiterator as lit

"""
  Este módulo implementa un iterador para recorrer los elementos
  de una lista encadenada
"""


def newIterator(lst):
    """
    Inicializa un iterador para la lista lst
    Args:
        lst: La lista sobre la que se quiere iterar
    Returns:
        Un iterador para la lista
    """
    if (lst['type'] == 'ARRAY_LIST'):
        return ait.newIterator(lst)
    else:
        return lit.newIterator(lst)


def hasNext(iterator):
    """
    Informa si se puede seguir iterando.
    Informa si existe un nodo en la siguiente posicion de la lista,
    a partir de la posicion actual del iterador.
    Args:
        iterator: El iterador creado sobre la lista
    Returns:
        True si existe un siguiente elemento, False de lo contrario
    """
    if (iterator['type'] == 'ARRAY_ITERATOR'):
        return ait.hasNext(iterator)
    else:
        return lit.hasNext(iterator)


def next(iterator):
    """
    Retorna el elemento en la posición siguiente a la indicada por el iterador
    Args:
        iterator: El iterador de la lista
    Returns:
        El siguiente elemento al último retornado por el iterador
    """
    if (iterator['type'] == 'ARRAY_ITERATOR'):
        return ait.next(iterator)
    else:
        return lit.next(iterator)
