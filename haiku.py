from colorama import init
init(autoreset=True)


# функция для подсчета слогов через гласные
def count_vowels(line):
    vowels = "аеёиоуыюяэ"
    count = 0
    for i in line.lower():
        if i in vowels:
            count += 1
    return count


# функция для проверки на хайку
def haiku_structure(haiku):
    syllable_number = [5, 7, 5]
    lines = haiku.split(" / ")

    if len(lines) != 3:
        result = '\n'.join(lines) + f"\n\033[31mНе хайку. Должно быть 3 строки.\n"
        return False, result

    for i in range(3):
        syllable = count_vowels(lines[i])
        if syllable != syllable_number[i]:
            result = '\n'.join(lines) + f"\n\033[31mНе хайку. В {i + 1} строке слогов не {syllable_number[i]}, а {syllable}.\n"
            return False, result

    result = '\n'.join(lines) + "\n\033[32mХайку!\n"
    return True, result


# читаем файлы для чтения и запичи 
with open('haiku.txt', 'r', encoding='utf-8') as inp_file:
    with open('test_haiku.txt', 'w', encoding='utf-8') as out_file:
        for line in inp_file:
            haiku = line.strip()

            # пропускаем пустые строки 
            if not haiku:
                continue

            is_valid, result = haiku_structure(haiku)
            print(result)
            out_file.write(result + "\n")
