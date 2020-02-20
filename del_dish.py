# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 13:39:22 2020
@author: 劉又聖
"""

from DataStructure import Dish
#from pick_dish import Pick_Dish
import json

def List_Dish(mode='1'):
    """
    Input,  mode,   為列出選擇類型
    Output, result, 為該次列出的所有菜色，方便後續刪除，需要在這邊回傳
    """
    func = {
        '1' : Get_Menu,    # 列出全部
        '2' : Pick_Dish,   # 列出部分，透過標籤篩選
    }
    
    idx    = 0
    result = func.get(mode, lambda:-1)()
    
    # 使用者輸入 1、2 以外的東西，回傳 -1 表示錯誤輸入
    # 否則應該回傳 list
    if result != -1:
        for dish in result:
            print(str(idx)+'.', dish)
            idx += 1
    
    return result


def Get_Menu(menu_name='menu.txt'):
    """
    Input,  menu_name, 這個我覺得不需要，可以再討論
    Output, result,    list of all dish
    """
    menu = []
    menu_s = json.load(open(menu_name, 'r'))
    for elem in menu_s:
        menu.append(Dish(*elem))
        
    return menu


def Del_Dish(menu, ID_list):
    """
    Input:
        menu is a list of all dish(Dish instance)
        ID_list is a list of index which all needs to pop
    """
    pass


def Delete_Dish():
    # 取得輸入，選擇列出類型(列出全部、使用標籤選擇)
    prompt = 'Input 1 for listing all dish to select, 2 for listing dish by tags to select.'
    choice = input(prompt)
    
    result = List_Dish(choice)  # 列出可選選項
    
    if result == -1:
        print(f'No {choice} this option')
        return False
    
    # 列出選擇後，取得使用者輸入，輸入為哪幾項需要刪除
    # 使用者輸入的是我們列出的index不等於dish的ID，需要轉換
    pass
    
    ID_list = ...
    
    # 執行刪除動作
    Del_Dish(...)    
    return True

Get_Menu()