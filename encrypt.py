# id133647009
"""Шифрованные инструкции."""
import string


def encrypting_instructions(instructions: str) -> str:
    """Программа для расшифровки сжатых сообщений."""
    stack_values: list = []
    part_instructions: str = ''
    multiplier: str = ''
    for symbol in instructions:
        match symbol:
            case _ if symbol in string.digits:
                multiplier += symbol
            case '[':
                stack_values.append((multiplier, part_instructions))
                part_instructions = multiplier = ''
            case ']':
                repeats, prev_command = stack_values.pop()
                part_instructions = (
                    prev_command + int(repeats) * part_instructions
                )
            case _:
                part_instructions += symbol
    return part_instructions


if __name__ == '__main__':

    print(encrypting_instructions(instructions=input()))
