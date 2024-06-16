"""Модуль обработки текстовой информации из видео"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english') +
                 list(string.punctuation) + ["’", "‘", "“", "”"])


def generate_tags(video_desc, audio_desc, user_desc):
    """
    Генерирует словарь тегов на основе текстовых данных видео, аудио и пользовательского описания.

    Аргументы:
        video_desc (str): Текстовое описание видеокомпонентов.
        audio_desc (str): Текстовое описание аудиокомпонентов.
        user_desc (str): Пользовательское описание видео.

    Возвращает:
        dict: Словарь с категориями и весами тегов.

    Пример:
        Входные данные: video_desc = "Cat playing", audio_desc = "Meowing", user_desc = "Funny cat video"
        Выходные данные: {'test': {'cat': 2, 'playing': 1, 'meowing': 1, 'funny': 1, 'video': 1}}
    """
    combined_description = f"{video_desc} {audio_desc} {user_desc}"
    words = word_tokenize(combined_description)

    filtered_words = [word.lower() for word in words if word.lower()
                      not in stop_words and len(word) > 1]

    tag_weights = {}
    for word in filtered_words:
        if word in tag_weights:
            tag_weights[word] += 1
        else:
            tag_weights[word] = 1

    categories_data = {
        "test": tag_weights
    }

    return categories_data
