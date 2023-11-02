def solution():
    # Calculate the number of years since Lydia planted the tree
    years_since_planted = 9 - 4

    # Calculate the number of years until the tree bears fruit
    years_until_fruit = 7 - years_since_planted % 7

    # Calculate the age Lydia will be when the tree bears fruit
    age_at_fruit = 9 + years_until_fruit

    result = age_at_fruit
    return result

print(solution())