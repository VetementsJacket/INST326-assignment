def question_validator(questions):
    """
    Checks question bank for missing or invalid information.
    
    Explanation by Group:
        
    Iterates through every question entry to ensure that all required keys and information are present. If invalid info is encountered, raises a descriptive exception explaining the problem so that invalid data does not cause errors during gameplay.
    
    Personal Notes (Rocco Lilli):
    
    Essentially, it takes the list that the JSON file was converted to in the last function I made, and pushes it through this system. I broke the questions down into obvious typical categories, ID to identify which question we were on, difficulty, category, question, answer. If any of those are formatted incorrectly, the question bank won't be accepted, and it will point the user to the exact index that their bank failed at.
        
    There is definetly multiple ways to do this, but I always think that listing everything out piece by piece is easiest for me to comprehend. Although I know that it is a headache for some that prefer more efficient ways of doing things, haha.
    
    Args:
        questions (list): list of questions to be validated.
    
    Returns:
        bool: True if all entries pass validation.
    
    Raises:
        ValueError: If a question contains invalid information.
        KeyError: If a question is missing one of the specified keys.
    
    Primary Author:
        Rocco Lilli
    
    """
    
    if not isinstance(questions, list):
        raise ValueError("Questions must be in list format. They should have been converted to a list before being passed to this function. Please check question bank.")
    
    if len(questions) == 0:
        raise ValueError("Looks like the question bank is empty! Add some questions!")
    
    needed_keys = {"id", "question", "diff", "category", "ans"}
    difficulties = {"easy", "medium", "hard"}
    
    for index, entry in enumerate(questions):
        if not isinstance(entry, dict):
            raise ValueError(f"Each question must be in the form of a dictionary. Error found at index {index}")
        missing_keys = needed_keys - entry.keys()
        if missing_keys:
            raise KeyError(f"Missing keys: {missing_keys}. Error found at index {index}. Please include the following keys: {needed_keys}.")
        if not isinstance(entry["id"], int):
            raise ValueError(f"Question ID must be an integer. Error found at index {index}. Please make sure that the question is represented by a whole number for it's ID.")
        if not isinstance(entry["question"], str):
            raise ValueError(f"Question text must be a string. Error found at index {index}. Make sure all questions make sense!")
        if entry["diff"] not in difficulties:
            raise ValueError(f"Difficulty must be {difficulties}. Error found at index {index}. No insane mode on this game!")
        if not isinstance(entry["category"], str):
            raise ValueError(f"Category must be formatted as a string. Error found at index {index}. I've never seen that category before... are you sure?")
        if not isinstance(entry["ans"], str):
            raise ValueError(f"Answer must be formatted as a string. Error found at index {index}. How will we defeat the boss with no answers!")
        
    return True