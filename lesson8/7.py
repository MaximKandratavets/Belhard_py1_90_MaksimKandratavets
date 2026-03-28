"""
Написать функцию (без регулярных выражений), которая принимает текстовую строку 
и возвращает словарь, который содержит информацию о количестве 
символов, слов, строк и предложений в тексте. 
Затем создайте вторую функцию, которая принимает этот словарь, 
и выводит его содержимое в удобном и красивом формате. 

"""

def analyze_text(text):
    symbols = len(text)
    words = len(text.split())
    lines = len(text.split('\n'))
    sentences = text.count('.') + text.count('!') + text.count('?')

    return {
        'symbols': symbols,
        'words': words,
        'lines': lines,
        'sentences': sentences
    }


def print_stats(stats):
    print("Анализ текста")
    print("-" * 20)
    print(f"Символов:      {stats['symbols']}")
    print(f"Слов:          {stats['words']}")
    print(f"Строк:         {stats['lines']}")
    print(f"Предложений:   {stats['sentences']}")


text = input("Введите текст: ")

result = analyze_text(text)
print_stats(result)