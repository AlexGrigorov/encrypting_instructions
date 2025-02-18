# id133633232
"""Шифрованные инструкции."""


def encrypting_instructions(instructions: str) -> str:
    """Программа для расшифровки сжатых сообщений."""
    list_of_tuples: list = []
    current_list: str = ''
    current_multiplier: str = ''
    numbers = '0123456789'
    for value in instructions:
        if value in numbers:
            current_multiplier += value
        elif value in '[':
            list_of_tuples.append((current_multiplier, current_list))
            current_list = ''
            current_multiplier = ''
        elif value in ']':
            previous_num, previous_str = list_of_tuples.pop()
            current_list = previous_str + int(previous_num) * current_list
        else:
            current_list += value
    return current_list


if __name__ == '__main__':

    print(encrypting_instructions(instructions=input()))
