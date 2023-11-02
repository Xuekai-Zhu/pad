def solution():
    # Calculate the total number of goals scored by both teams in the whole match
    first_half_A = 8  # Team A scored 8 points in the first half
    first_half_B = 4  # Team B scored half as many points as Team A in the first half
    second_half_A = first_half_B + 2  # Team A scored 2 goals less than Team B in the second half
    second_half_B = first_half_A  # Team B scored as many points as Team A in the first half
    total_goals = first_half_A + first_half_B + second_half_A + second_half_B
    result = total_goals
    return result

print(solution())