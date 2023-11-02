def solution():
    total_earnings = 400  # The bake sale earns $400 in total
    cost_of_ingredients = 100  # Andrew keeps $100 to cover the cost of ingredients
    remaining_total = total_earnings - cost_of_ingredients  # Calculate the remaining total after cost of ingredients

    # Calculate the amount donated to each charity
    donation_to_homeless_shelter = (remaining_total / 2) + 10  # Andrew donates half of the remaining total plus $10 from his piggy bank
    donation_to_food_bank = remaining_total / 2

    result = donation_to_homeless_shelter  # The amount donated to the homeless shelter
    return result

print(solution())