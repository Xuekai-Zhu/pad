def solution():
    num_kittens = 4
    num_adult_cats = 3
    num_cans = 7

    # Calculate the total number of cans needed each day
    total_cans_per_day = num_adult_cats + (num_kittens * 0.75)

    # Calculate the total number of cans needed for 7 days
    total_cans_7_days = total_cans_per_day * 7

    # Calculate the additional cans of food that need to be bought
    additional_cans = total_cans_7_days - num_cans

    result = additional_cans
    return result

print(solution())