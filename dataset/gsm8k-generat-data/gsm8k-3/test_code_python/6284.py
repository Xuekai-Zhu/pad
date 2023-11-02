def solution():
    """Lola and Tara decide to race to the top of a 20 story building. Tara takes the elevator and Lola runs up the stairs. Lola can run up 1 story in 10 seconds. The elevator goes up a story in 8 seconds but stops for 3 seconds on every single floor. How long would it take for the slower one of Lola and Tara to reach the top floor?"""
    # Define values
    num_stories = 20
    lola_time = num_stories * 10
    tara_time = (num_stories * 8) + (num_stories * 3)

    # Determine the slower one's time
    slower_time = max(lola_time, tara_time)

    # Display the slower one's time
    result = slower_time
    return result

print(solution())