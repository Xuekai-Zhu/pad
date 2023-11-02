def solution():
    rolls_of_paper = 3
    gifts_wrapped = 12
    gifts_wrapped_roll_1 = 3
    gifts_wrapped_roll_2 = 5
    gifts_wrapped_roll_3 = gifts_wrapped - gifts_wrapped_roll_1 - gifts_wrapped_roll_2
    result = gifts_wrapped_roll_3
    return result

print(solution())