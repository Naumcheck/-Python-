'''

Антон учится в karpov.courses. В словаре anton_courses хранится информация о завершенных им курсах и количестве набранных баллов. 
Данные в словаре хранятся в формате ключ — название курса, значение — количество баллов в числовом формате. 
Антон завершил обучение на курсе HardML и набрал 120 баллов. Добавьте в словарь anton_courses эту информацию. 
В переменную courses сохраните список пройденных курсов. 
В переменную StartML сохраните количество баллов, набранное Антоном на одноименном курсе, эта информация есть в словаре. 



Пример: 

anton_courses = {'SimulatorAnalyst': 56, 
                 'StartML': 87, 
                 'DataAnalyst': 140}
# -> 
anton_courses = {'SimulatorAnalyst': 56, 
                 'StartML': 87, 
                 'DataAnalyst': 140, 
                 'HardML': 120}
courses = ['SimulatorAnalyst', 'StartML', 'DataAnalyst', 'HardML']
StartML = 87

'''
anton_courses['HardML'] = 120
courses = list(anton_courses.keys())
StartML = anton_courses['StartML']