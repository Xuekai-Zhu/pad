def solution():
    # Calculate the cost of buying eggs per week
    cost_of_eggs = 2/12  # $2 for one dozen eggs

    # Calculate the cost of keeping the chickens per week
    cost_of_chickens = (4 * 1) + 1  # 4 chickens at $20 each, plus $1 for their feed

    # Calculate the number of weeks it will take for the chickens to be cheaper than buying eggs
    eggs_per_week = 12  # 1 dozen eggs
    eggs_per_chicken_per_week = 3/4  # each chicken produces 3 eggs a week
    savings_per_week = (eggs_per_week * cost_of_eggs) - (eggs_per_chicken_per_week * cost_of_chickens)

    weeks = 20 / savings_per_week  # the cost of buying the 4 chickens

    result = weeks
    return result

print(solution())