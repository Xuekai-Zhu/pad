def solution():
    """Kylie picks apples for 3 hours. The first hour she picks 66 apples. The second hour she doubles her apple picking rate, and the third hour she picks a third of the apples picked in the first hour. How many apples did Kylie pick total?"""
    hour1_picked = 66
    hour2_picked = 2 * hour1_picked
    hour3_picked = hour1_picked / 3
    total_picked = hour1_picked + hour2_picked + hour3_picked
    result = total_picked
    return result

print(solution())