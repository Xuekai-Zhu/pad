def solution():
    """Joan has 2 hours to get all her music practice done. She spends 30 minutes on the piano, 25 minutes writing music on her computer, and 38 minutes reading about the history of the piano. Her final work is to use a special finger exerciser. How much time does she have left to use this?"""
    # Define the total time available in minutes
    total_time = 2 * 60

    # Calculate the time spent on piano, computer, and reading
    piano_time = 30
    computer_time = 25
    reading_time = 38

    # Calculate the total time spent on these activities
    total_spent_time = piano_time + computer_time + reading_time

    # Calculate the time left for finger exercises
    finger_exercises_time = total_time - total_spent_time

    result = finger_exercises_time
    return result

print(solution())