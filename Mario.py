def filter_questions(difficulty):

    question_bank = [{"difficulty":3}]

    filtered_questions = []

    for question in question_bank:
        if question["difficulty"] == difficulty:
            filtered_questions.append(question)

    return filtered_questions 

print(filter_questions(3))
