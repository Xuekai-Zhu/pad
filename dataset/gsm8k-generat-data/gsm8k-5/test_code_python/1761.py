def solution():
    total_crates = 50  # Kevin sells a total of 50 crates of fruit per week
    grapes_crates = 13  # Kevin sold 13 crates of grapes
    mangoes_crates = 20  # Kevin sold 20 crates of mangoes

    # Calculate the number of passion fruit crates Kevin sold
    passion_fruits_crates = total_crates - grapes_crates - mangoes_crates
    result = passion_fruits_crates
    return result

print(solution())