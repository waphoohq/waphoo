import random
from games_project_pleshakova.VD_games.cli import welcome_user, get_user_answer


def is_even(number):
    """Проверяет, является ли число чётным."""
    return number % 2 == 0


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    correct_answers = 0
    total_questions = 3
    
    while correct_answers < total_questions:
        # Генерируем случайное число
        number = random.randint(1, 100)
        print(f'Question: {number}')
        
        # Получаем ответ от пользователя
        user_answer = get_user_answer()
        
        # Определяем правильный ответ
        correct_answer = 'yes' if is_even(number) else 'no'
        
        # Проверяем ответ
        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
