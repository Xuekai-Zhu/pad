def solution():
    # Calculate how much money Bob had left after Monday
    money_left_monday = 80 / 2

    # Calculate how much money he had left after Tuesday
    money_left_tuesday = money_left_monday - (money_left_monday / 5)

    # Calculate how much money he had left after Wednesday
    money_left_wednesday = money_left_tuesday - ((3/8) * money_left_tuesday)

    result = money_left_wednesday
    return result

print(solution())