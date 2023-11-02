def solution():
    """Rose had 10 kilograms of rice. She cooked 9/10 kilograms in the morning and 1/4 of the remaining in the evening. How many grams of rice did she have left?"""
    starting_amount = 10000 # convert to grams
    morning_cooked = 9/10 * starting_amount
    remaining_rice = starting_amount - morning_cooked
    evening_cooked = 1/4 * remaining_rice
    amount_left = remaining_rice - evening_cooked
    result = amount_left
    return result

print(solution())