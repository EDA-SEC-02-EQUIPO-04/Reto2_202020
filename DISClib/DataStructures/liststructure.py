"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
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

import config
from DISClib.Utils import error as error
from DISClib.DataStructures import arraylist as alt
from DISClib.DataStructures import singlelinkedlist as slt

assert config

"""
  Este módulo selecciona la estructura de datos deseada para ejectuar
  una operación del TAD Lista.
"""


def newList(datastructure='SINGLE_LINKED', cmpfunction=None):
    """Crea una lista vacia.

    Args:
        cmpfunction: Función de comparación para los elementos de la lista
    Returns:
        Una nueva lista
    Raises:
        Exception
    """
    try:
        if (datastructure == "ARRAY_LIST"):
            lt = alt.newList(cmpfunction)
        else:
            lt = slt.newList(cmpfunction)
        return lt
    except Exception as exp:
        error.reraise(exp, 'list->newList: ')


def addFirst(lst, element):
    """Agrega un elemento a la lista en la primera posicion.

    Agrega un elemento en la primera posición de la lista, se incrementa
    el tamaño de la lista en uno.

    Args:
        lst:  La lista don de inserta el elemento
        element:  El elemento a insertar en la lista

    Returns:
        La lista con el nuevo elemento en la primera posición,
        si el proceso fue exitoso

    Raises:
        Exception
    """
    try:
        if (lst['type'] == 'ARRAY_LIST'):
            alt.addFirst(lst, element)
        else:
            slt.addFirst(lst, element)
    except Exception as exp:
        error.reraise(exp, 'List->addFirst: ')


def addLast(lst, element):
    """ Agrega un elemento en la última posición de la lista.

    Se adiciona un elemento en la última posición de la lista y se actualiza
    el apuntador a la útima posición.
    Se incrementa el tamaño de la lista en 1

    Args:
        lst: La lista en la que se inserta el elemento
        element: El elemento a insertar

    Raises:
        Exception
    """
    try:
        if (lst['type'] == 'ARRAY_LIST'):
            alt.addLast(lst, element)
        else:
            slt.addLast(lst, element)
    except Exception as exp:
        error.reraise(exp, 'List->addLast: ')


def isEmpty(lst):
    """ Indica si la lista está vacía

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        if (lst['type'] == 'ARRAY_LIST'):
            return alt.isEmpty(lst)
        else:
            return slt.isEmpty(lst)
    except Exception as exp:
        error.reraise(exp, 'List->isEmpty: ')


def size(lst):
    """ Informa el número de elementos de la lista.

    Args
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        if (lst['type'] == 'ARRAY_LIST'):
            return alt.size(lst)
        else:
            return slt.size(lst)
    except Exception as exp:
        error.reraise(exp, 'List->size: ')


def firstElement(lst):
    """ Retorna el primer elemento de una lista no vacía.
        No se elimina el elemento.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        if (lst['type'] == 'ARRAY_LIST'):
            return alt.firstElement(lst)
        else:
            return slt.firstElement(lst)
    except Exception as exp:
        error.reraise(exp, 'List->firstElement: ')


def lastElement(lst):
    """ Retorna el último elemento de una  lista no vacia.
        No se elimina el elemento.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        if (lst['type'] == 'ARRAY_LIST'):
            return alt.lastElement(lst)
        else:
            return slt.lastElement(lst)
    except Exception as exp:
        error.reraise(exp, 'List->lastElement: ')


def getElement(lst, pos):
    """ Retorna el elemento en la posición pos de la lista.

    Se recorre la lista hasta el elemento pos, el cual  debe ser mayor
    que cero y menor o igual al tamaño de la lista.
    Se retorna el elemento en dicha posición sin eleminarlo.
    La lista no puede ser vacia.

    Args:
        lst: La lista a examinar
        pos: Posición del elemento a retornar

    Raises:
        Exception
    """
    try:
        if (lst['type'] == 'ARRAY_LIST'):
            return alt.getElement(lst, pos)
        else:
            return slt.getElement(lst, pos)
    except Exception as exp:
        error.reraise(exp, 'List->getElement: ')


def deleteElement(lst, pos):
    """ Elimina el elemento en la posición pos de la lista.

    Elimina el elemento que se encuentra en la posición pos de la lista.
    Pos debe ser mayor que cero y menor o igual al tamaño de la lista.
    Se decrementa en un uno el tamñao de la lista.
    La lista no puede estar vacia.

    Args:
        lst: La lista a retoranr
        pos: Posición del elemento a eliminar.

    Raises:
        Exception
    """
    try:
        if (lst['type'] == 'ARRAY_LIST'):
            alt.deleteElement(lst, pos)
        else:
            slt.deleteElement(lst, pos)
    except Exception as exp:
        error.reraise(exp, 'List->deleteElement: ')


def removeFirst(lst):
    """ Remueve el primer elemento de la lista.

    Elimina y retorna el primer elemento de la lista.
    El tamaño de la lista se decrementa en uno.
    Si la lista es vacía se retorna None.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        if (lst['type'] == 'ARRAY_LIST'):
            return alt.removeFirst(lst)
        else:
            return slt.removeFirst(lst)
    except Exception as exp:
        error.reraise(exp, 'List->removeFirst: ')


def removeLast(lst):
    """ Remueve el último elemento de la lista.
    Elimina el último elemento de la lista  y lo retorna en caso de existir.
    El tamaño de la lista se decrementa en 1.
    Si la lista es vacía  retorna None.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        if (lst['type'] == 'ARRAY_LIST'):
            return alt.removeLast(lst)
        else:
            return slt.removeLast(lst)
    except Exception as exp:
        error.reraise(exp, 'List->removeLast: ')


def insertElement(lst, element, pos):
    """ Inserta el elemento element en la posición pos de la lista.

    Inserta el elemento en la posición pos de la lista.
    La lista puede ser vacía.
    Se incrementa en 1 el tamaño de la lista.

    Args:
        lst: La lista en la que se va a insertar el elemento
        element: El elemento a insertar
        pos: posición en la que se va a insertar el elemento,
        0 < pos <= size(lst)

    Raises:
        Exception
    """
    try:
        if (lst['type'] == 'ARRAY_LIST'):
            alt.insertElement(lst, element, pos)
        else:
            slt.insertElement(lst, element, pos)
    except Exception as exp:
        error.reraise(exp, 'List->insertElement: ')


def isPresent(lst, element):
    """ Informa si el elemento element esta presente en la lista.

    Informa si un elemento está en la lista.
    Si esta presente, retorna la posición en la que se encuentra
    o cero (0) si no esta presente.
    Se utiliza la función de comparación utilizada durante la creación
    de la lista para comparar los elementos.

    Args:
        lst: La lista a examinar
        element: El elemento a buscar

    Raises:
        Exception
    """
    try:
        if (lst['type'] == 'ARRAY_LIST'):
            return alt.isPresent(lst, element)
        else:
            return slt.isPresent(lst, element)
    except Exception as exp:
        error.reraise(exp, 'List->isPresent: ')


def exchange(lst, pos1, pos2):
    """ Intercambia la informacion en las posiciones pos1 y pos2 de la lista.
    Args:
        lst: La lista a examinar
        pos1: Posición del primer elemento
        pos2: Posiocion del segundo elemento

    Raises:
        Exception
    """
    try:
        if (lst['type'] == 'ARRAY_LIST'):
            alt.exchange(lst, pos1, pos2)
        else:
            slt.exchange(lst, pos1, pos2)
    except Exception as exp:
        error.reraise(exp, 'List->exchange: ')


def changeInfo(lst, pos, element):
    """ Cambia la informacion contenida en el nodo de la lista que se
        encuentra en la posicion pos.

    Args:
        lst: La lista a examinar
        pos: la posición de la lista con la información a cambiar
        newinfo:
        La nueva información que se debe poner en el nodo de la posición pos

    Raises:
        Exception
    """
    try:
        if (lst['type'] == 'ARRAY_LIST'):
            alt.changeInfo(lst, pos, element)
        else:
            slt.changeInfo(lst, pos, element)
    except Exception as exp:
        error.reraise(exp, 'List->changeInfo: ')


def subList(lst, pos, numelem):
    """ Retorna una sublista de la lista lst.

    Se retorna una lista que contiene los elementos a partir de
    la posicion pos, con una longitud de numelem elementos.
    Se crea una copia de dichos elementos y se retorna una lista nueva.

    Args:
        lst: La lista a examinar
        pos: Posición a partir de la que se desea obtener la sublista
        numelem: Numero de elementos a copiar en la sublista

    Raises:
        Exception
    """
    try:
        if (lst['type'] == 'ARRAY_LIST'):
            return alt.subList(lst, pos, numelem)
        else:
            return slt.subList(lst, pos, numelem)
    except Exception as exp:
        error.reraise(exp, 'List->subList: ')
