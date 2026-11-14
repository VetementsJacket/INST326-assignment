import random


def shuffle_answers(correct_answer, incorrect_answers):
    """
    Randomizes the display order of multiple-choice answers.

    It combines the correct answer with all other incorrect answer choices
    into a single list. Then it utilizes a randomization process to shuffle
    the positions of the answers so that players can't memorize
    the correct answer's letter or position.

    Args:
        correct_answer (str): The correct answer to the question.
        incorrect_answers (list): A collection of incorrect answers.

    Returns:
        list: A shuffled list that which contains the correct answer and
        all incorrect answer choices.

    Primary Author:
        Deivy Casso II
    """

    if not isinstance(correct_answer, str) or correct_answer == "":
        raise ValueError("Correct answer have to be a non-empty string.")

    if not isinstance(incorrect_answers, list) or len(incorrect_answers) == 0:
        raise ValueError("Incorrect answers have to be a non-empty list.")

    answers = [correct_answer]

    for answer in incorrect_answers:
        if not isinstance(answer, str) or answer == "":
            raise ValueError("All answers are only non-empty strings.")

        if answer in answers:
            raise ValueError("No Duplicate answers.")

        answers.append(answer)

    random.shuffle(answers)

    return answers

