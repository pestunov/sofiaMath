#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#Created on May 25, 2021
#@author: Pestunov Doma
#

import telebot
import time
import mysecure
import random

def generateTask(_order):
    ii = random.randint(1,_order)
    jj = random.randint(1,_order)
    if ii >= jj:
        strr = ('{} - {} = ?'.format(ii,jj))
        answer = dif(ii,jj)
    else:
        strr = ('{} + {} = ?'.format(ii,jj))
        answer = summ(ii,jj)
    return (strr, answer)

def dif(a,b):
#    return '...'
    return a-b

def summ(a,b):
#    return '...'
    return a+b

def generateAnswer(_answer, _num):
    res = [str(_answer + random.randint(int(-_answer/2), int(_answer/2))) for _ in range(_num)]
    pos = random.randint(0,_num-1)
    res[pos] = str(_answer)
    return res

level = {'easiest': 10,
         'easy': 20,
         'good': 50,
         'math': 100,
         'math die': 500,
         'koval':1000}

NNN = level['math']
cyc = norder = 0

bot = telebot.TeleBot(mysecure.telebotToken)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('ясельки', 'детсад', 'первоклашка')
keyboard1.row('институт','академег', 'ковалевская')

@bot.message_handler(commands=['start'])
def start_message(message):
    global cyc
    bot.send_message(message.chat.id, 'Привет {}, займемся математикой'.format(message.from_user.first_name))
    bot.send_message(message.chat.id, 'Выбери уровень'.format(message.from_user.first_name), reply_markup=keyboard1)
    cyc = 1

@bot.message_handler(content_types=['text'])
def send_text(message):
    global cyc,  norder
    if cyc == 1:
        if message.text.lower() == 'ясельки':
            bot.send_message(message.chat.id, 'ну ладно, малыш, поехали...')
            norder = level['easiest']
            cyc = 2
        if message.text.lower() == 'детсад':
            bot.send_message(message.chat.id, 'в школу захотелось? давай попробуем...')
            norder = level['easy']
            cyc = 2
        if message.text.lower() == 'первоклашка':
            bot.send_message(message.chat.id, 'вперед школота-та!!!')
            norder = level['good']
            cyc = 2
        if message.text.lower() == 'институт':
            bot.send_message(message.chat.id, 'давай всех порвем')
            norder = level['math']
            cyc = 2
        if message.text.lower() == 'академег':
            bot.send_message(message.chat.id, 'ты сам напросился...')
            norder = level['math die']
            cyc = 2
        if message.text.lower() == 'ковалевская':
            bot.send_message(message.chat.id, 'сейчас ты подотрешься...')
            norder = level['koval']
            cyc = 2

    if cyc == 2:
        strr, answer = generateTask(norder)
        a1, a2, a3, a4, a5, a6 = generateAnswer(answer, 6)

        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row(a1, a2, a3)
        keyboard.row(a4, a5, a6)
        keyboard.row('сдаюсь', '/start')
        bot.send_message(message.chat.id, strr, reply_markup=keyboard)
        if message.text.lower() == str(answer):
            bot.send_message(message.chat.id, 'Правильно')
            

        

    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай')
#     else:
#         textt = message.text.upper()
#         bot.send_message(message.chat.id, 'что это? {}'.format(textt))
        
bot.polling(none_stop = False)

