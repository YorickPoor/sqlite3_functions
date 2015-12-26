#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sqlite3
import os


def createBase(path):
    """
    path = path to database
    """""""""
    path = os.path.abspath(path)
    base = sqlite3.connect(path)
    base.close()


def createTableInBase(path, args):
    """
    args = [
    'table_name',
    "1_row row_type some conditions,
     2_row row_type some conditions,
     n_row row_type some conditions,
     ..."]
    """
    path = os.path.abspath(path)
    base = sqlite3.connect(path)
    cursor = base.cursor()
    str_execute = 'CREATE TABLE {} ({})'.format(*args)
    try:
        cursor.execute(str_execute)
        base.commit()
        base.close()
        return True
    except:
        base.close()
        return False


def addDataToTable(path, args):
    """
    args = ['table_name',
    "row_name1,
     row_name2,
     row_namen...",
    "row_value1,
     row_value2,
     row_valuen..."]
     or
     args = ['table_name',
    "row_value1,
     row_value2,
     row_valuen..."]
    """
    path = os.path.abspath(path)
    base = sqlite3.connect(path)
    cursor = base.cursor()
    if len(args) == 3:
        str_execute = 'INSERT INTO {} ({}) VALUES({})'.format(*args)
    elif len(args) == 2:
        str_execute = 'INSERT INTO {} VALUES({})'.format(*args)
    try:
        cursor.execute(str_execute)
        base.commit()
        base.close()
        return True
    except:
        base.close()
        return False


def selectDataFromTable(path, args):
    """
    args = ['row-1 , row-2, row-n',
            'table_name',
            'condition']
    or
    args = ['row-1 , row-2, row-n',
            'table_name']
    """""""""
    path = os.path.abspath(path)
    base = sqlite3.connect(path)
    cursor = base.cursor()
    if len(args) == 2:
        str_execute = 'SELECT {} FROM {}'.format(*args)
    elif len(args) == 3:
        str_execute = 'SELECT {} FROM {} WHERE {}'.format(*args)
    try:
        cursor.execute(str_execute)
        data = cursor.fetchall()
        base.commit()
        base.close()
        return data
    except:
        base.close()
        return False


def updateDataInTable(path, args):
    """
    args = ['table_name',
            'row_name',
            'new_data on row',
            'condition']
    or
    args = ['table_name',
            'row_name',
            'new_data on row',
            'row_name',
            'old_data_on_row']
    """
    path = os.path.abspath(path)
    base = sqlite3.connect(path)
    cursor = base.cursor()
    if len(args) == 4:
        str_execute = 'UPDATE {} SET {} = {} WHERE {}'.format(*args)
    elif len(args) == 5:
        str_execute = 'UPDATE {} SET {} = {} WHERE {} = {}'.format(*args)
    try:
        cursor.execute(str_execute)
        base.commit()
        base.close()
        return True
    except:
        base.close()
        return False


def delDataInTable(path, args):
    """
    args = ['table_name',
            'conditions']
    or
    args = ['table_name',
            'row_name',
            'row_data']
    """
    path = os.path.abspath(path)
    base = sqlite3.connect(path)
    cursor = base.cursor()
    if len(args) == 2:
        str_execute = 'DELETE FROM {} WHERE {}'.format(args)
    elif len(args) == 3:
        str_execute = 'DELETE FROM {} WHERE {} = {}'.format(args)
    try:
        cursor.execute(str_execute)
        base.commit()
        base.close()
        return True
    except:
        base.close()
        return False


def addNewColumnInTable(path, args):
    """
    args = ['table_name',
            'New_column_name',
            'type of new column']
    """
    path = os.path.abspath(path)
    base = sqlite3.connect(path)
    cursor = base.cursor()
    str_execute = 'ALERT TABLE {} ADD COLUMN {} {}'
    try:
        cursor.execute(str_execute)
        base.commit()
        base.close()
        return True
    except:
        base.close()
        return False


def renameTableInBase(path, old_name, new_name):
    path = os.path.abspath(path)
    base = sqlite3.connect(path)
    cursor = base.cursor()
    str_execute = 'ALERT TABLE {} RENAME TO {}'.format(old_name, new_name)
    try:
        cursor.execute(str_execute)
        base.commit()
        base.close()
        return True
    except:
        base.close()
        return False


def deleteTableInBase(path, table_name):
    path = os.path.abspath(path)
    base = sqlite3.connect(path)
    cursor = base.cursor()
    str_execute = 'DROP TABLE {}'.format(table_name)
    try:
        cursor.execute(str_execute)
        base.commit()
        base.close()
        return True
    except:
        base.close()
        return False
