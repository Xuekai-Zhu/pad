def solution():
    total_crates_per_week = 50
    grapes_sold = 13
    mangoes_sold = 20

    # Calculate the total number of passion fruit crates sold
    passion_fruit_sold = total_crates_per_week - grapes_sold - mangoes_sold
    result = passion_fruit_sold
    return result

print(solution())