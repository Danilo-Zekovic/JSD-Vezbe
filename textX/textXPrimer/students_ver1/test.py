'''
Created on 06.12.2015.

@author: xx
'''


from execute import execute as ex
import os

ex.execute(os.path.split(__file__)[0], 'students.tx', 'example.students', True, True)