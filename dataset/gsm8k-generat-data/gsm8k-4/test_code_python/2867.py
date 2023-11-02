def solution():
    """Micah, Dean, and Jake are all training for a marathon organized by a local NGO to support children in their town who have cancer. Micah runs 2/3 times as fast as Dean. It takes Jake 1/3 times more time to finish the marathon than it takes Mica. If Dean takes 9 hours, what's the total time the three take to complete the marathon?"""
    # Define the time taken by Dean to finish the marathon
    dean_time = 9

    # Calculate the time taken by Micah to finish the marathon
    micah_time = (2/3) * dean_time

    # Calculate the time taken by Jake to finish the marathon
    jake_time = micah_time * (4/3)

    # Calculate the total time taken by all three to finish the marathon
    total_time = dean_time + micah_time + jake_time

    # Return the result
    result = total_time
    return result

print(solution())