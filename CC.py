# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 13:10:05 2017

@author: pabeni
"""
'''
# with class
import CCFunctionDef
person = CCFunctionDef.Account('Lala', '123-567', 1000 )
person.doExercise( 200 )
person.eatMeal( 300 )
print( person )
'''

'''
# not class
import CCFunctionDef
person = CCFunctionDef.account( 'Lala', '123-567', 1000 )
CCFunctionDef.doExercise( person, 200 )
CCFunctionDef.eatMeal( person, 300 )
print( CCFunctionDef.to_str( person ) )
'''