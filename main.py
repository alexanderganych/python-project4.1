import random
import string
from functools import reduce


def actions_with_words(text, n_word, action):
    """Функция для генерации случайных слов

    Атрибуты:
    n_text - количество символов в text;
    n_word - количество слов;
    actions - действия над словами;
    text - случайно сгенерированная последовательность букв и цифр;
    text_list - text разбитый на n_word пробелов
    places_space_random - позиция случайного пробела в переменной text;
    temp_text - временная переменная для text.
    """
    # Количество символов
    n = len(text)

    # Определим случайные места для пробелов, чтобы получить n_word слов
    # Если рядом есть пробелы, то слов получится меньше
    # Поэтому и отказался от выражения ниже:
    # places_space_random = random.sample(range(n), n_word - 1)

    # Этим способом получилось избежать проблемы соседних пробелов:
    places_space_random = []
    while len(places_space_random) < n_word - 1:
        place = random.randint(0, n - 1)
        if (place not in places_space_random and
            (place + 1) not in places_space_random and
            (place - 1) not in places_space_random and
            # Пробелы не должны стоять в самом начале и конце
            place != 0 and
            place != n - 1):
            places_space_random.append(place)

    # Заменим часть символом в text на пробел, чтобы получилось n_word слов
    for i in range(n_word - 1):
        # Заменим символ на place_space_random на пробел
        temp_text = list(text)
        temp_text[places_space_random[i]] = ' '
        text = ''.join(temp_text)

    # Преобразуем строку в список
    print(f"\nСгенерированны {n_word} слов из строки имеющей {n} символов:\n{text}")
    text_list = text.split()

    # Количество операция
    n_action = len(action)
    for i in range(n_word):
        # Формируем индекцсы для операций так, чтобы выполнялись поочереди
        index_for_action = i % n_action

        match action[index_for_action]:
            case 'upper':
                print("\n'upper' - сделать все буквы заглавными:")
                print("До:\n", text_list[i])
                text_list[i] = upper_action(text_list[i])
                print("После:\n", text_list[i])
            case 'reverse':
                print("\n'reverse' - слово в обратном порядке:")
                print("До:\n", text_list[i])
                text_list[i] = reverse_action(text_list[i])
                print("После:\n", text_list[i])
            case 'double':
                print("\n'double' - продублировать слово (станет слово + это же слово) :")
                print("До:\n", text_list[i])
                text_list[i] = double_action(text_list[i])
                print("После:\n", text_list[i])
            case 'del_digits':
                print("\n'del_digits' - удалить из слова цифры:")
                print("До:\n", text_list[i])
                text_list[i] = del_digits_action(text_list[i])
                print("После:\n",text_list[i])
            case 'del_even':
                print("\n'del_even' - удалить каждый чётный символ:")
                print("До:\n", text_list[i])
                text_list[i] = del_even_action(text_list[i])
                print("После:\n", text_list[i])
            case 'replace':
                print("\n'replace' - заменить каждую цифру слова на 'Python':")
                print("До:\n", text_list[i])
                text_list[i] = replace_action(text_list[i])
                print("После:\n", text_list[i])
            case _:
                print("\nНеизвестная операция!")

    return text, reduce(lambda concat_word, word: concat_word + word + ' ',
                        text_list, '').strip()

upper_action = lambda word: word.upper()

reverse_action = lambda word: word[::-1]

double_action = lambda word: word + word

def del_digits_action(word):
    """Удаляем из полученного слова цифры.

    Атрибут:
    word - слово из которого удалим цифры
    char - отдельный символ слова word
    """
    return ''.join(filter(lambda char: char.isalpha(), word))

del_even_action = lambda word: word[::2]

def replace_action(word):
    '''Заменяем каждую цифру на слово "Puthon"

    Атрибуты:
    word - слово в котором будем делать замену
    char - символ каждого слова
    '''
    return ''.join(map(lambda char: 'Python' if char.isdigit() else char, word))

# Количество символов
n = 1000

# Количество слов
n_word = 10

# Кортеж действий над словами
actions = ('upper', 'reverse', 'double', 'del_digits', 'del_even', 'replace')

# Генерируем исходный текст
text = ''.join([random.choice(string.ascii_letters + string.digits)
                for i in range(n)])

text_initial, text_after_actions = actions_with_words(text, n_word, actions)

print(f"\nСтрока после разделения на {n_word} пробел(-а, -ов):\n", text_initial)
print("\nИтоговый результат:\n", text_after_actions)