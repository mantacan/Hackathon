import uuid
from flask import Flask, request, jsonify
from video_processing.input import Input

app = Flask(__name__)

@app.route('/processing', methods=['POST'])
def handle_post():
    """
    Обрабатывает POST-запрос, содержащий JSON-данные. Данные должны быть представлены в виде списка словарей,
    каждый из которых содержит ключи 'id', 'url' и 'description'.

    Процесс обработки:
    1. Проверяет, что полученные данные являются списком.
    2. Для каждого элемента в списке проверяет наличие всех требуемых ключей.
    3. Создаёт экземпляр класса `Input` для каждого элемента, обрабатывает его и получает теги.
    4. Собирает результаты в виде списка словарей с ключами 'id', 'url', и 'tags'.
    5. Возвращает JSON-ответ со статусом 200 и результатами в случае успеха, либо со статусом 400 или 500 в случае ошибки.

    Возвращает:
        JSON-объект со статусом 200 и информацией об успешной обработке запроса.
        В случае неверного формата данных возвращает JSON-объект с ошибкой и статусом 400.
        В случае ошибок при обработке возвращает JSON-объект с описанием ошибки и статусом 500.

    Примеры возвращаемых значений:
        - При успешной обработке: {'message': 'GOOD', 'results': [{'id': 1, 'url': 'example.com', 'tags': ['tag1', 'tag2']}]}
        - При ошибке формата данных: {'error': 'Expected data to be a list'}, статус 400
        - При ошибке обработки: {'error': 'описание ошибки'}, статус 500
    ---
    tags:
      - Video Processing
    parameters:
      - in: body
        name: body
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: The ID of the video.
              url:
                type: string
                description: The URL of the video.
              description:
                type: string
                description: Description of the video.
    responses:
      200:
        description: Video processed successfully.
      400:
        description: Error with input data format.
      500:
        description: Internal server error.
    """
    data = request.get_json()

    # Проверка, что данные являются объектом, а не массивом
    if not isinstance(data, dict):
        return jsonify({"error": "Expected data to be an object"}), 400

    # Проверка наличия необходимых ключей
    if not all(key in data for key in ['url', 'description']):
        return jsonify({"error": "Object must contain 'url' and 'description'"}), 400

    try:
        # Генерация случайного id
        data_id = str(uuid.uuid4())

        # Создаем экземпляр класса Input
        input_instance = Input(data['url'], data['description'])
        # Обрабатываем запрос и получаем теги
        tags = input_instance.proceed()
        result = {
            "id": data_id,
            "url": data['url'],
            "tags": tags
        }
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "GOOD", "result": result}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
