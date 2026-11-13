from Hassen import update_player_progress

# Test 1: Correct answer reduces boss health
assert update_player_progress("easy", 3, True) == ("easy", 2, "playing")

# Test 2: Defeating a boss advances difficulty
assert update_player_progress("easy", 1, True) == ("medium", 3, "playing")

# Test 3: Wrong answer lowers difficulty
assert update_player_progress("hard", 2, False) == ("medium", 3, "playing")

# Test 4: Defeating the final boss wins the game
assert update_player_progress("hard", 1, True) == ("hard", 0, "victory")

print("All tests passed!")
