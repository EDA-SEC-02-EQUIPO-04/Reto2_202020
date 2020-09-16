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
from DISClib.DataStructures import listnode as node
from DISClib.Utils import error as error

assert config

"""
  Este módulo implementa una estructura de datos lineal mediante una lista
  encadenada sencillamente para almacenar una colección de elementos.
  Los elementos se cuentan desde la posición 1.
"""


def newList(cmpfunction=None):
    """Crea una lista vacia.

    Se inicializan los apuntadores a la primera y ultima posicion en None.
    El tipo de la listase inicializa como SINGLE_LINKED
    Args:
        cmpfunction: Función de comparación para los elementos de la lista
    Returns:
        Un diccionario que representa la estructura de datos de una lista
        encadanada vacia.

    Raises:

    """
    new_list = {'first': None,
                'last': None,
                'size': 0,
                'type': 'SINGLE_LINKED',
                'cmpfunction': cmpfunction}
    return new_list


def addFirst(lst, element):
    """Agrega un elemento a la lista en la primera posicion.

    Agrega un elemento en la primera posición de la lista, ajusta el apuntador
    al primer elemento e incrementa el tamaño de la lista.

    Args:
        lst:  La lista don de inserta el elemento
        element:  El elemento a insertar en la lista

    Returns:
        La lista con el nuevo elemento en la primera posición, si el proceso
        fue exitoso

    Raises:
        Exception
    """
    try:
        new_node = node.newSingleNode(element)
        new_node['next'] = lst['first']
        lst['first'] = new_node
        if (lst['size'] == 0):
            lst['last'] = lst['first']
        lst['size'] += 1
        return lst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->addFirst: ')


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
        new_node = node.newSingleNode(element)

        if lst['size'] == 0:
            lst['first'] = new_node
        else:
            lst['last']['next'] = new_node
        lst['last'] = new_node
        lst['size'] += 1
        return lst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->addLast: ')


def isEmpty(lst):
    """ Indica si la lista está vacía
    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        return lst['size'] == 0
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->isEmpty: ')


def size(lst):
    """ Informa el número de elementos de la lista.
    Args
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        return lst['size']
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->size: ')


def firstElement(lst):
    """ Retorna el primer elemento de una lista no vacía.
     No se elimina el elemento.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        if 'info' in lst['first']:
            return lst['first']['info']
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->fisrtElement: ')


def lastElement(lst):
    """ Retorna el último elemento de una  lista no vacia.
        No se elimina el elemento.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        if 'info' in lst['last']:
            return lst['last']['info']
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->lastElement: ')


def getElement(lst, pos):
    """ Retorna el elemento en la posición pos de la lista.

    Se recorre la lista hasta el elemento pos, el cual  debe ser
    mayor que cero y menor o igual al tamaño de la lista.
    Se retorna el elemento en dicha posición sin eleminarlo.
    La lista no puede ser vacia.

    Args:
        lst: La lista a examinar
        pos: Posición del elemento a retornar

    Raises:
        Exception
    """
    try:
        searchpos = 1
        node = lst['first']
        while searchpos < pos:
            searchpos += 1
            node = node['next']
        return node['info']
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->getElement: ')


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
        node = lst['first']
        prev = lst['first']
        searchpos = 1
        if (pos == 1):
            lst['first'] = lst['first']['next']
        elif (pos > 1):
            while searchpos < pos:
                searchpos += 1
                prev = node
                node = node['next']
            prev['next'] = node['next']
        lst['size'] -= 1
        return lst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->deleteElement: ')


def removeFirst(lst):
    """ Remueve el primer elemento de la lista.
    Elimina y retorna el primer elemento de la lista.
    El tamaño de la lista se decrementa en uno.  Si la lista
    es vacía se retorna None.
    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        if lst['first'] is not None:
            temp = lst['first']['next']
            node = lst['first']
            lst['first'] = temp
            lst['size'] -= 1
            if (lst['size'] == 0):
                lst['last'] = lst['first']
            return node['info']
        else:
            return None
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->removeFirst: ')


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
        if lst['size'] > 0:
            if lst['first'] == lst['last']:
                node = lst['first']
                lst['last'] = None
                lst['first'] = None
            else:
                temp = lst['first']
                while temp['next'] != lst['last']:
                    temp = temp['next']
                node = lst['last']
                lst['last'] = temp
                lst['last']['next'] = None
            lst['size'] -= 1
            return node['info']
        else:
            return None
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->remoLast: ')


def insertElement(lst, element, pos):
    """ Inserta el elemento element en la posición pos de la lista.

    Inserta el elemento en la posición pos de la lista.
    La lista puede ser vacía.  Se incrementa en 1 el tamaño de la lista.

    Args:
        lst: La lista en la que se va a insertar el elemento
        element: El elemento a insertar
        pos: posición en la que se va a insertar el elemento,
        0 < pos <= size(lst)

    Raises:
        Exception
    """
    try:
        new_node = node.newSingleNode(element)
        if (pos == 1):
            new_node['next'] = lst['first']
            lst['first'] = new_node
        else:
            cont = 1
            prev = lst['first']
            current = lst['first']
            while cont < pos:
                prev = current
                current = current['next']
                cont += 1
            new_node['next'] = current
            prev['next'] = new_node
        lst['size'] += 1
        return lst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->insertElement: ')


def isPresent(lst, element):
    """ Informa si el elemento element esta presente en la lista.

    Informa si un elemento está en la lista.  Si esta presente,
    retorna la posición en la que se encuentra  o cero (0) si no esta presente.
    Se utiliza la función de comparación utilizada durante la creación
    de la lista para comparar los elementos.
    La cual debe retornar cero en caso de que los elementos sean iguales.

    Args:
        lst: La lista a examinar
        element: El elemento a buscar

    Raises:
        Exception
    """
    try:
        size = lst['size']
        if size > 0:
            node = lst['first']
            keyexist = False
            for keypos in range(1, size + 1):
                if (lst['cmpfunction'](element, node['info']) == 0):
                    keyexist = True
                    break
                node = node['next']
            if keyexist:
                return keypos
        return 0
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->isPresent: ')


def changeInfo(lst, pos, newinfo):
    """ Cambia la informacion contenida en el nodo de la lista que se encuentra
         en la posicion pos.

    Args:
        lst: La lista a examinar
        pos: la posición de la lista con la información a cambiar
        newinfo: La nueva información que se debe poner en el nodo de
        la posición pos

    Raises:
        Exception
    """
    try:
        current = lst['first']
        cont = 1
        while cont < pos:
            current = current['next']
            cont += 1
        current['info'] = newinfo
        return lst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->changeInfo: ')


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
        infopos1 = getElement(lst, pos1)
        infopos2 = getElement(lst, pos2)
        changeInfo(lst, pos1, infopos2)
        changeInfo(lst, pos2, infopos1)
        return lst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->exchange: ')


def subList(lst, pos, numelem):
    """ Retorna una sublista de la lista lst.

    Se retorna una lista que contiene los elementos a partir de la
    posicion pos,con una longitud de numelem elementos.
    Se crea una copia de dichos elementos y se retorna una lista nueva.

    Args:
        lst: La lista a examinar
        pos: Posición a partir de la que se desea obtener la sublista
        numelem: Numero de elementos a copiar en la sublista

    Raises:
        Exception
    """
    try:
        sublst = {'first': None,
                  'last': None,
                  'size': 0,
                  'type': 'SINGLE_LINKED',
                  'cmpfunction': lst['cmpfunction']}
        cont = 1
        loc = pos
        while cont <= numelem:
            elem = getElement(lst, loc)
            addLast(sublst, elem)
            loc += 1
            cont += 1
        return sublst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->subList: ')
