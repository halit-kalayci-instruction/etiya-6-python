# classes.py içindeki Human'ı kullan
#import classes => tüm classes modülünü import eder
from classes import Human #=> classes modülünden Human'ı import
import random #pythondaki hazır modüller
import openpyxl
#Alias => takma ad
# from classes import Human as Insan
#import classes as Classlarim

human1 = Human("Halit",25)
human1.talk("Selam")

print(random.random())

