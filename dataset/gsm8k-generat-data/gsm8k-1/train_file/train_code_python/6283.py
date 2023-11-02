def solution():
    """Lola and Tara decide to race to the top of a 20 story building. Tara takes the elevator and Lola runs up the stairs. Lola can run up 1 story in 10 seconds. The elevator goes up a story in 8 seconds but stops for 3 seconds on every single floor. How long would it take for the slower one of Lola and Tara to reach the top floor?"""
    stories = 20
    stairs_time = stories * 10
    elevator_time = (stories * 8) + (stories * 3)
    slowest_time = max(stairs_time, elevator_time)
    result = slowest_time
    return result

print(solution())