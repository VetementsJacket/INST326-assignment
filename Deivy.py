import random


# Function 1: Shuffle Answer Choices
def shuffle_answers(correct_answer, incorrect_answers):
    """
    Randomizes the display order of multiple-choice answers.

    Combines the correct answer with all incorrect answer choices
    into a single list. Uses a randomization process to shuffle
    the positions of the answers so that players cannot memorize
    the correct answer's letter or position.

    Args:
        correct_answer (str): The correct answer to the question.
        incorrect_answers (list): A collection of incorrect answers.

    Returns:
        list: A shuffled list containing the correct answer and
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


# Function 2: Map Correct Answer Index
def find_correct_index(shuffled_answers, correct_answer):
    """
    Finds and records the correct answer's position after shuffling.

    Searches through the randomized answer list to identify the
    position of the correct answer. Records its index so the game
    can compare the player's selection against the correct answer.

    Args:
        shuffled_answers (list): The randomized collection of answers.
        correct_answer (str): The correct answer to the question.

    Returns:
        int: The index position of the correct answer.

    Raises:
        ValueError: If the correct answer cannot be found in the
        shuffled answer collection.

    Primary Author:
        Deivy Casso II
    """

    if not isinstance(shuffled_answers, list):
        raise ValueError("Shuffled answers must be a list.")

    for index, answer in enumerate(shuffled_answers):
        if answer == correct_answer:
            return index

    raise ValueError("Correct answer was not found in the shuffled answers.")
