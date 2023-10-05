
import os
path = '/Users/polina/Documents/Python_Lab/Programm-lab '
projectname = 'dataset*'
folders = \
[ '*dog*', 
 '*cat*']

fullPath = os.path.join(path,projectname)
os.mkdir(fullPath)


