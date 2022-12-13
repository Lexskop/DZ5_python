# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.
# Пример:
# Пугать ты галок пугай => заданная строка "галок" => Пугать ты пугай
# Пугать ты галок пугай => заданная строка "пуг" => Пугать ты галок

input_data=input('Введите текст -> \n').split()
input_word=input('Введите слово для удаления ->\n')

def delete_selected_text(input_data:list,input_word:str) -> str:
    """
    Удаляет из принятого текста заданную строку
    """
    output_text=''
    for i in range(len(input_data)):
        if str(input_data[i]).find(input_word) == -1:
            output_text+=input_data[i]+ ' '
    return output_text

print(delete_selected_text(input_data,input_word))