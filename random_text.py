import random

from math import floor
from math import ceil
from typing import Union

vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
letters = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'a', 'e', 'i', 'o', 'u']


def get_random_word(length: int) -> str:
    result = get_successor(None)
    for i in range(1, length):
        result += get_successor(result[i - 1])
    return result


def get_successor(prev_char: Union[str, None]) -> str:
    if prev_char is None:
        return letters[random.randint(0, len(letters) - 1)]
    elif prev_char in consonants:
        return vowels[random.randint(0, len(vowels) - 1)]
    else:
        return [x for x in letters if x != prev_char][random.randint(0, len(letters) - 2)]


def generate_sentence(min_words: int, max_words: int) -> str:
    sentence = ""
    num_words = random.randint(min_words, max_words + 1)
    for i in range(0, num_words):
        sentence += get_random_word(random.randint(3, 10))

        if i != num_words - 1:
            sentence += ' '

    sentence += "." if random.randint(0, 100) > 20 else "!"

    return sentence


def generate_text(num_sentences: int, min_words_per_sentence: int = 3, max_words_per_sentence: int = 10) -> str:
    text = ""
    for _ in range(0, num_sentences):
        text += generate_sentence(min_words_per_sentence,
                                  max_words_per_sentence)

        if random.randint(0, 100) > 30:
            text += ' '
        else:
            text += '\n'

    return text


def generate_text_to_file(filename: str, num_sentences: int, min_words_per_sentence: int = 3, max_words_per_sentence: int = 10):
    text = generate_text(
        num_sentences,
        min_words_per_sentence,
        max_words_per_sentence)
    file_to_write = open(filename, "a")
    file_to_write.write(text)
    file_to_write.close()
