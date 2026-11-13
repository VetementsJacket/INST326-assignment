def filter_questions(difficulty):

    filtered_questions = []

    for question in question_bank:
        if question["difficulty"] == difficulty:
            filtered_questions.append(question)

    return filtered_questions
