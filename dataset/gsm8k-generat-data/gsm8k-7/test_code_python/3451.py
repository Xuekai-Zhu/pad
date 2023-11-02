def solution():
    green_beans_weight = 60  # given in the question
    sugar_weight = green_beans_weight - 10  # given in the question
    rice_weight = sugar_weight - 30  # given in the question

    # Calculate the weight of lost rice and sugar
    lost_rice_weight = (1 / 3) * rice_weight
    lost_sugar_weight = (1 / 5) * sugar_weight

    # Calculate the remaining weight of rice and sugar
    remaining_rice_weight = rice_weight - lost_rice_weight
    remaining_sugar_weight = sugar_weight - lost_sugar_weight

    # Calculate the total weight of the remaining stock
    total_weight = remaining_rice_weight + green_beans_weight + remaining_sugar_weight
    result = total_weight
    return result

print(solution())