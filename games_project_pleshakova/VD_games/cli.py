import prompt


def welcome_user():
    """Приветствует пользователя и возвращает его имя."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_user_answer():
    """Получает ответ от пользователя."""
    return prompt.string('Your answer: ')
