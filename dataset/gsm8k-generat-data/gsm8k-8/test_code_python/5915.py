def solution():
    # Define the variables and their values
    initial_crates = 6
    crates_given_away = 2
    crates_bought = 5
    eggs_per_crate = 30

    # Calculate the total number of eggs
    total_eggs = (initial_crates - crates_given_away + crates_bought) * eggs_per_crate

    result = total_eggs
    return result

print(solution())