import threading

# Создание файла и запись в файл списка студентов
file = open('files for serching/group_1.txt', mode='w', encoding='utf')
file.writelines([
                '1. Дьомшина Анастасія Миколаївна 335\n', 
                '2. Войтенко Артем Анатолійович 278\n',
                '3. Судніцин Дмитро Вікторович 273\n',
                '4. Нікітченко Руслан Ігорович 165\n',
                '5. Яковенко Дмитро Володимирович 217\n',
                '6. Пискун Сергій Юрійович 188\n',
                '7. Каштаєв Артур Віталійович 186\n',
                '8. Гончаров Роман Костянтинович 243\n',
                '9. Денисенко Ростислав Васильович 126\n',
                '10. Якубік Артем Андрійович 126\n'
                ])
file.close()

file = open('files for serching/group_2.txt', mode='w', encoding='utf')
file.writelines([
                '1. Дьомшина Анастасія Миколаївна 335\n', 
                '2. Войтенко Артем Анатолійович 278\n',
                '3. Судніцин Дмитро Вікторович 273\n',
                '4. Денисенко Ростислав Васильович 126243\n',
                '5. Гончаров Яковенко Дмитро Володимирович 217\n',
                '6. Пискун Сергій Юрійович 188\n',
                '7. Каштаєв Артур Віталійович 186\n',
                '8. Нікітченко Руслан Ігорович 165\n',
                '9. Гончаров Роман Костянтинович\n',
                '10. Якубік Артем Андрійович 126\n'
                ])
file.close()

value = 1

serchingText = input('Введите слово для поиска - ')

def serching(fileName, serchingText):
    global value
    with open(fileName, 'r+', encoding='utf') as file_1:
        elements = file_1.readlines()
        for i in range(len(elements)):
            if value == 0:
                return 0
            elif serchingText in elements[i].split(' '):
                value = 0
                return print(f'Номер строки - {i}; Текст запроса - {serchingText}; Имя файла - {fileName}')
        return print(f'запрашиваемое слово отсутствует в файле {fileName}')

potoc_1 = threading.Thread(target = serching, args=('files for serching/group_1.txt', serchingText))
potoc_2 = threading.Thread(target = serching, args=('files for serching/group_2.txt', serchingText))

potoc_1.start()
potoc_2.start()

potoc_1.join() 
potoc_2.join()



