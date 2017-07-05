# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 13:08:30 2017

@author: pabeni
"""

'''
# not class
# CC = CalorieCalculator
def account(name, ID, balance):
    print('現有 %d 的熱量' % balance)
    return {'name': name, 'ID': ID, 'balance': balance}

def doExercise( person, CC):
    print('消耗 %d 的熱量' % CC)
    if CC > person['balance']:
        raise Warning('運動過量了')
    person['balance'] += CC

def eatMeal( person, CC):
    print('補充 %d 的熱量' % CC)
    if CC <= 0:
        raise Warning('吃太少了')
    person['balance'] -= CC
  
def to_str( person ):
    return 'CC is ' + str(person) + ' now.'

'''    




'''
# class
class Account:
    def __init__( self, name, ID, balance ):
        self.name = name
        self.ID = ID
        self.balance = balance
    
    def doExercise(self, CC):
        print('消耗 %d 的熱量' % CC)
        if CC > self.balance:
            raise Warning('運動過量了')
        self.balance += CC
        
    def eatMeal( self, CC ):
        print('補充 %d 的熱量' % CC)
        if CC <= 0:
            raise Warning('吃太少了')
        self.balance -= CC
        
    def __str__(self):
        return 'Account({0}, {1}, {2})'.format(\
            self.name, self.ID, self.balance)
'''