def solution():
    # Calculate the total number of cans of cat food needed for 7 days
    total_cans_needed = (3 * 7) + (4 * 7 * 3/4)  # 3 adult cats eat 1 can per day, 4 kittens eat 3/4 of a can per day for 7 days
    cans_already_owned = 7  # Sidney has 7 cans of cat food

    # Calculate the additional cans of cat food Sidney needs to buy
    additional_cans_needed = total_cans_needed - cans_already_owned
    result = additional_cans_needed
    return result

print(solution())