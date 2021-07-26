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

def _():
    pass

level = {'easiest': 10,
         'easy': 20,
         'good': 50,
         'math': 100,
         'math die': 500,
         'koval':1000}

NNN = level['math']
cyc = norder = score = countt = 0
answer = 0

bot = telebot.TeleBot(mysecure.telebotToken)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('ясельки', 'детсад', 'первоклашка')
keyboard1.row('институт','академег', 'ковалевская')

@bot.message_handler(commands=['start'])
def start_message(message):
    global cyc,  norder, answer, countt, score
    bot.send_message(message.chat.id, 'Привет {}, займемся математикой. Выбери уровень, гений!'.format(message.from_user.first_name))
    cyc = 1
    countt = 10

@bot.message_handler(content_types=['text'])
def send_text(message):
    global cyc,  norder, answer, countt, score
    if cyc == 2:
        if message.text.lower() in ['сдаюсь', 'дальше']:
            bot.send_message(message.chat.id, '{}, слабак'.format(answer))
        elif message.text.lower() == str(answer):
            bot.send_message(message.chat.id, 'правильно')
            countt -= 1
            score +=1
        else:
            bot.send_message(message.chat.id, 'упс! {}'.format(answer))
            countt -= 1
            score -=2
        
        if countt == 0:
            bot.send_message(message.chat.id, 'все! ты набрал {} баллов'.format(score))
            cyc = 3
        else:
            strr, answer = generateTask(norder)
            strr = f'{countt}) {strr}'
            a1, a2, a3, a4, a5 = generateAnswer(answer, 5)
            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            keyboard.row(a1, a2, a3, a4, a5)
            keyboard.row('сдаюсь', '/start')
            bot.send_message(message.chat.id, strr, reply_markup=keyboard)
            
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
            a1, a2, a3, a4, a5 = generateAnswer(answer, 5)
            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            keyboard.row(a1, a2, a3, a4, a5)
            keyboard.row('сдаюсь', '/start')
            bot.send_message(message.chat.id, strr, reply_markup=keyboard)



        

    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай')
#     else:
#         textt = message.text.upper()
#         bot.send_message(message.chat.id, 'что это? {}'.format(textt))
        
bot.polling(none_stop = True)
