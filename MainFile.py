#НАПИСАТЬ ШИФРАТОР И РАБОТУ С НИМ
#НАПИСАТЬ ВСЕ ЧЕРЕЗ ФУНКЦИИ
#ИСПРАВИТЬ БАГ КУРСОРА
import os
def pretty_lines(text, sym_in_line):
                    Line_len = len(text)//sym_in_line+2
                    Text_Massive = list(text)
                    for i in range(Line_len):
                        Text_Massive.insert((sym_in_line+1)*i, '\n')
                    return ''.join(Text_Massive)
def pointer_print(pointer_place, text, sym_in_line):
    Massive_text = list(text)
    if pointer_place>=0:
        Seeker_place = pointer_place
    else:
        Seeker_place = len(text)+pointer_place
    Massive_text.insert((Seeker_place//sym_in_line+1)*sym_in_line, '\n' + Seeker_place%sym_in_line*' ' + '^ Your pointer here \n')
    return print(pretty_lines(Massive_text, sym_in_line))
work = True
while work:
    dir = input('Please enter directory of the document:\n')
    dir = r'{}'.format(dir)
    while not os.path.exists(dir):
        dir = input('Please enter existing directory of a document:\n')
        dir = r'{}'.format(dir)
    os.chdir(dir)
    print('List of files and directories:\n' + '\n'.join(os.listdir(dir)))
    doc_name = input('Enter document name to edit: ')

#проверка имени документа
    while doc_name == '':
        doc_name = input('ENTER document name: ')
    
#проверка существования документа и в случае его отсутствия - создание
    try :
        file = open(dir + r'\{}'.format(doc_name), 'r')
        print('The text in the document now is following: \n'+ pretty_lines(file.read(), 60))
        file.close()
    except FileNotFoundError:
        file = open(dir + r'\{}'.format(doc_name), 'w')
        file.close()
        print('The document is empty')
#выбор действия над документом
    choice = input('Choose between EDIT, WIPE or OVERWRITE the document: ')
    while choice.lower() not in ['edit', 'overwrite', 'wipe', 'e', 'o', 'w']:
        choice = input('EDIT, WIPE or OVERWRITE: ')
#редактирование
    if choice.lower() in ['edit', 'e']:
        editing_state = True
        first_time = True
        while editing_state:
            if first_time:                              #если документ еще не находится в процессе редактирования, то
                file = open(dir + r'\{}'.format(doc_name), 'r')  
                text = file.read()
                text_len = len(text)
                file.close()
            else:                                       #если документ уже находится в процессе редактирования
                text = final
                text_len = len(final)
            string_len=str(text_len)
#отображение редактируемого текста
            print('Now the text is following:', pretty_lines(text, 60), sep = '\n')
#ввод положения указателя
            pointer = input('Please enter the number of symbol between \'0\' and '+ '\'' + string_len + '\' from where to write or delete: ')
#проверка введенного указателя
            while pointer.strip('-1234567890') != '' or pointer == '' or pointer.endswith('-') or abs(int(pointer))>text_len:
                print('tadam, you\'re wrong')
                pointer = input('Please enter the NUMBER of symbol from where to write/delete: ')
            pointer = int(pointer)
            pointer_print(pointer, text, 60) #отображение указателя
#/редактирование/ выбор записи или удаления символов
            write_or_del = input('Choose write or delete? ')
            while write_or_del.lower() not in ['w', 'd', 'write', 'delete']: #проверка введенного значения
                write_or_del = input('Choose write or delete')
            editing = list(text)
#/редактирование/запись
            if write_or_del in ['w', 'write']:
                a = input('Enter text: ') 
                editing.insert(pointer, a) #ввод текста в промежуточную память
#/редактирование/удаление
            else:
                sym_to_del = input('Enter number of symbols to delete: ') #проверка числа ПЕРЕПИСАТЬ ЧЕРЕЗ ФУНКЦИЮ
                while sym_to_del.strip('-1234567890') != '' or sym_to_del == '' or sym_to_del.endswith('-'):
                    print('tadam, you\'re wrong')
                    sym_to_del = input('Enter number of symbols to delete: ')
                sym_to_del = int(sym_to_del)
                del editing[text_len+pointer:text_len+pointer+sym_to_del]
#/редактирование/создание финального образа
            final = ''.join(editing)
            continiue_editing = input('Continiue editing? ')
            while continiue_editing.lower() not in ['no', 'n', 'yes', 'y']:
                continiue_editing = input('Answer yes/no: ')
            if continiue_editing.lower() in ['no', 'n']:
                editing_state = False
            else:
                first_time = False
#перезапись
    elif choice.lower() in ['overwrite', 'o']:
        final = input('Enter text to overwrite: ')
#вайп
    elif choice.lower() in ['wipe', 'w']:
        final = ''
#изменение файла
    file = open(dir + r'\{}'.format(doc_name), 'w')
    file.write(final)
    file.close()
#отображение результата
    file = open(dir + r'\{}'.format(doc_name), 'r') 
    print('Now the text in the file is following: ' + pretty_lines(file.read(), 60))
    file.close()
#продолжение работы с приложением
    continiue_work = input('Do you want to change something else? ')
    while continiue_work.lower() not in ['yes', 'y', 'no', 'n']:
        continiue_work = input('Choose between \"yes\" or \"no\": ')
    if continiue_work.lower() in ['no', 'n']:
        work = False
