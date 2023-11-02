def solution():
    """Lola and Tara decide to race to the top of a 20 story building. Tara takes the elevator and Lola runs up the stairs. Lola can run up 1 story in 10 seconds. The elevator goes up a story in 8 seconds but stops for 3 seconds on every single floor. How long would it take for the slower one of Lola and Tara to reach the top floor?"""

    # Calculate the time it takes for Lola to reach the top floor
    lola_time = 20 * 10

    # Calculate the time it takes for Tara to reach the top floor
    tara_time = 0

    for i in range(1, 21):
        tara_time += 8 # Time to ascend 1 story
        if i != 20:
            tara_time += 3 # Time for the elevator to stop

    # Determine the slowest time and return the result
    slowest_time = max(lola_time, tara_time)

    return slowest_time

print(solution())