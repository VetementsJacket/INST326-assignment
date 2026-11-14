def filter_questions(difficulty):
    """Will filter the main question bank according to the player's
    current difficulty tier.

    Will search the question bank and creates a smaller collection
    containing only questions that match the player's current
    difficulty level.

    Args:
        difficulty (int): The player's current difficulty tier.

    Returns:
        list: A collection of questions matching the specified
            difficulty level.

    Primary Author:
        Mario Chacon.
    """

    question_bank = [
        {"question": "What does print() do?",
        "correct_answer": "Displays output",
        "incorrect_answers": [
            "Deletes the code", "Returns a value", "Imports a module"],
        "difficulty":2},
        {"question": "What is a variable?",
        "correct_answer": "A named location which stores a value",
        "incorrect_answers": ["A loop", "A function", "A module"],
        "difficulty": 1},
        {"question": "What is inheritance?",
         "correct_answer": "A class receiving properties from another class",
         "incorrect_answers": ["Syntax Error", "A type of loop", "A statement"],
         "difficulty":3}
        ]

    filtered_questions = []

    for question in question_bank:
        if question["difficulty"] == difficulty:
            filtered_questions.append(question)

    return filtered_questions 

print(filter_questions(3))
