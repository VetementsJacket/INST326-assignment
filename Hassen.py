def update_player_progress(difficulty, boss_health, correct):
    """
    Updates the player's progress after answering a question.

    Correct answers reduce the boss's health.
    Incorrect answers lower the difficulty tier.
    Defeating a boss advances the player to the next tier.

    Args:
        difficulty (str): Current difficulty level.
        boss_health (int): Remaining boss health.
        correct (bool): Whether the answer was correct.

    Returns:
        tuple: Updated difficulty, boss health, and game status.

    Primary Author:
        Hassen Said.
    """

    difficulties = ["easy", "medium", "hard"]

    if difficulty not in difficulties:
        raise ValueError("Invalid difficulty level.")

    if not isinstance(correct, bool):
        raise ValueError("Correct must be True or False.")

    if not isinstance(boss_health, int) or not 1 <= boss_health <= 3:
        raise ValueError("Boss health must be between 1 and 3.")

    # Find the player's current difficulty tier
    for index, level in enumerate(difficulties):
        if level == difficulty:
            current_tier = index
            break

    if correct:
        boss_health -= 1
        print("Correct! Boss takes 1 damage.")

        if boss_health == 0:
            if current_tier == len(difficulties) - 1:
                print("Congratulations! You defeated the final boss!")
                return difficulty, 0, "victory"

            difficulty = difficulties[current_tier + 1]
            boss_health = 3
            print(f"Boss defeated! Advancing to {difficulty}.")

    else:
        print("Incorrect answer!")

        if current_tier > 0:
            difficulty = difficulties[current_tier - 1]
            print(f"Moving back to {difficulty}.")
        else:
            print("Already at the easiest difficulty.")

        boss_health = 3

    print(f"Difficulty: {difficulty}")
    print(f"Boss Health: {boss_health}/3")

    return difficulty, boss_health, "playing"