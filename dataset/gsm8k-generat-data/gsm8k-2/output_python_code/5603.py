def solution():
    """During a soccer game, in the first half, Team A scored 8 points, and Team B scored only half as many points. In the second half, Team B was able to get as many points as Team A in the first half, and Team A scored only 2 goals less than Team B. How many goals did both teams score during the whole match?"""
    first_half_a = 8
    first_half_b = first_half_a / 2
    second_half_b = first_half_a
    second_half_a = second_half_b + 2
    total_goals = first_half_a + first_half_b + second_half_a + second_half_b
    result = total_goals
    return result

print(solution())