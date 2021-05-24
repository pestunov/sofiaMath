import random

level = {'easiest': 10,
         'easy': 20,
         'good': 50,
         'math': 100,
         'math die': 500}
NNN = level['math']

def dif(a,b):
    return '...'
#    return a-b

def summ(a,b):
    return '...'
#    return a+b

def generateTask():
    ii = random.randint(1,NNN)
    jj = random.randint(1,NNN)
    if ii >= jj:
        return('{} - {} = {}'.format(ii,jj, dif(ii,jj)))
    return('{} + {} = {}'.format(ii,jj, summ(ii,jj)))

for i in range(32):
    print(generateTask(), end = '\t\t')
    print(generateTask(), end = '\t\t')
    print(generateTask(), end = '\t\t')
    print(generateTask())
