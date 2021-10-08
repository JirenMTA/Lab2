#ФИО: Фам Нгок Хунг
#№ Группа 6112
# Вариант 112
import json
import re
import time
from tqdm import tqdm

class Validator:
  '''
  Объект класса Validator  
  Он нужен для того, что проверить данные валидными или нет
  '''

  def check_telephone(telephone) -> bool:
    '''
    Выполняет проверку корректности номера телефона
    Если телефон не иммет вид '+7-(111)-222-33-44' то будет возвращено False
    
    Параметры
    ---------
      telephone: 
        параметр для проверки корректности
    
    Return
    ------ 
      bool: 
        Булевый результат на коррестность
    '''
    if type(telephone) != str:
       return False
    pattern = '\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}'
    if re.match(pattern, telephone):
      return True
    return False

  def check_height(height : str) -> bool:
    '''
    Выполняет проверку корректности массы
    Если масса нет строки вида '1.22' или больше '2.51' то будет ворвращено False
    
    Параметры
    ---------
      height : str
        Параметр для проверки корректности
        
    Return 
    ------
      bool:
        Булевый результат на коррестность
    '''
    pattern = '[1-2]\.\d{2}'
    if re.match(pattern, str(height)) != None:
      if float(height) < 2.51:
        return True
    return False

  def check_inn(inn : str) -> bool:
    '''
    Выполняет проверку корректности ИНН
    Если ИНН не состоит из последовательности 12 цифр то возвращено False 
    
    Параметры
    ---------
      inn : str
        Строка для проверки корректности
        
    Return
    ------
      bool:
        Булевый результат на корректность
    '''
    if len(inn) == 12:
      return True
    return False

  def check_passport(passport : int) -> bool:
    '''
      Выполняет проверку корректности номера паспорта
      Если номер паспорта не состоит из последовательности 6 цифр то возвращено False
      
      Параметры
      ---------
        passport : int
          Целое число для проверки корректности
      
      Return
      ------
         bool:
           Булевый результат на корректность
      '''
    if len(str(passport)) == 6:
      return True
    return False
  
  def check_address(address) -> bool:
    '''
      Выполняет проверку корректности адреса
      Если адрес нет строки или указан не в формате "улица пробел номер дома" то возвращено False
      
      Параметры
      ---------
        address:
          Параметр для проверки корректности
          
      Return
      ------
        bool:
          Булевый результат на корректность
    '''
    pattern = '[а-яА-Я.\s\d-]+\s+[0-9]+$'
    if type(address) != str:
      return False
    if re.match(pattern, address):
      return True
    return False

  def check_type_int(number) -> bool:
    '''
      Выполняет проверку типа данных параметра
      Если пераметр не имеет тип данных int то возвращено False
      
      Параметры
      ---------
        number:
          Параметр для проверки типа данных
      
      Return
      ------
        bool:
          Булевый результат на корректность
    '''
    if type(number) == int:
      return True
    return False

  def check_type_string(string) -> str:
    '''
      Выполняет проверку типа данных параметра
      Если пераметр не имеет тип данных str возвращено False
      
      Параметры
      ---------
        string:
          Параметр для проверки типа данных
      
      Return
      ------
        bool:
          Булевый результат на корректность
    '''
    if type(string) != str:
      return False
    return True

path = 'D:\\112.txt'
data = json.load(open(path, encoding='windows-1251'))

true_data = list()
telephone = 0
height = 0
passport = 0
address = 0
work_experience = 0
inn = 0
university = 0
worldview = 0
political_view = 0
with tqdm(total = len(data)) as progressbar:
    for person in data:
      temp = True
      if Validator.check_telephone(person['telephone']) == False:
        telephone += 1
        temp = False
      if Validator.check_height(person['height']) == False:
        height += 1
        temp = False
      if Validator.check_inn(person['inn']) == False:
        inn += 1
        temp = False
      if Validator.check_passport(person['passport_number']) == False:
        passport += 1
        temp = False
      if Validator.check_address(person["address"]) == False:
        address += 1
        temp = False
      if Validator.check_type_int(person['work_experience']) == False:
        work_experience += 1
        temp = False
      if Validator.check_type_string(person['university']) == False:
        university += 1
        temp = False
      if Validator.check_type_string(person['political_views']) == False:
        political_view += 1
        temp = False
      if Validator.check_type_string(person['worldview']) == False:
        worldview += 1
        temp = False
      if temp == True:
        true_data.append(person)
      progressbar.update(1)


#print (f'{telephone} {height} {inn} {passport} {university} {work_experience} {political_view}  {worldview}  {address}')

path = 'out_put.txt'
out_put = open(path, 'w', encoding = 'utf-8')
beauty_data = json.dumps(true_data, ensure_ascii = False, indent = 4)
#json.dump(beauty_data, out_put, ensure_ascii = False)
out_put.write(beauty_data)
out_put.close()

print(f'Число валидных записей: {len(true_data)}')
print(f'Число невалидныч записей: {len(data) - len(true_data)}')
print(f'  - Число невалидных номеров телефона:  {telephone}')
print(f'  - Число невалидных масс: {height}')
print(f'  - Число невалидных ИНН: {inn}')
print(f'  - Число невалидных номеров паспорта: {passport}')
print(f'  - Число невалидных университетов: {university}')
print(f'  - Число невалидных рабочих стажей: {work_experience}')
print(f'  - Число невалидных политических взглядов: {political_view}')
print(f'  - Число невалидных мировоззрений: {worldview}')
print(f'  - Число невалидных адрессов: {address}')
print('\n*Замечание: каждый человек может быть иметь несколько невалидых записей')
!autopep8 --in-place --aggressive --aggressive uglycodesample.py
