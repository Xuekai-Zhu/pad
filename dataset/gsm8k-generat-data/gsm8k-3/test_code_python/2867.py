def solution():
    """Micah, Dean, and Jake are all training for a marathon organized by a local NGO to support children in their town who have cancer. Micah runs 2/3 times as fast as Dean. It takes Jake 1/3 times more time to finish the marathon than it takes Mica. If Dean takes 9 hours, what's the total time the three take to complete the marathon?"""
    # Define the time it takes for Dean to complete the marathon
    dean_time = 9

    # Calculate the time it takes for Micah to complete the marathon
    micah_time = (2/3) * dean_time

    # Calculate the time it takes for Jake to complete the marathon
    jake_time = micah_time * (4/3)

    # Calculate the total time it takes for all three to complete the marathon
    total_time = dean_time + micah_time + jake_time

    # Display the total time
    result = total_time
    return result

print(solution())