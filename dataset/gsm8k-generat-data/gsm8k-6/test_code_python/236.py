def solution():
    # Calculate Jake's remaining money
    money_left = 5000 - 2800  # Jake spends $2800 on a new motorcycle
    money_left = money_left / 2  # Jake spends half of what's left on a concert ticket
    money_left = money_left * (3/4)  # Jake loses a fourth of what he has left

    result = money_left
    return result

print(solution())