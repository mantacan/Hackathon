"""Контроллер парсера видео"""


from video_processing.processing import Processing


class Input:
    """
    Класс для обработки валидности входных данных пользователя и парсинга компонентов видео в теги.
    Объект класса принимает URL видео и описание, обрабатывает видео, и возвращает теги в формате JSON.

    Атрибуты:
        request (str): URL видео, которое необходимо обработать.
        description (str): Описание видео, добавляемое в теги.

    Методы:
        verify_request: Проверяет корректность URL (не реализовано).
        proceed: Обрабатывает видео и возвращает теги в формате JSON.
    """

    def __init__(self, url: str, description: str):
        self.request = url
        self.description = description

    def verify_request(self):
        """WIP: Метод отвечающий за обработку и верификацию входных данных"""
        pass

    def proceed(self):
        """
        Обрабатывает видео и возвращает теги в формате JSON.

        Возвращает:
            dict: Теги видео в формате JSON.
        """
        tags = Processing(self.request).process()
        tags.set_description_data(self.description)
        tags.set_video_url(self.request)

        return tags.generate_json()


def main():
    """Функция позволяющая воспользоваться парсером не используя сервер"""
    url = input()
    desc = input()
    print(Input(url, desc).proceed())


if __name__ == "__main__":
    main()
