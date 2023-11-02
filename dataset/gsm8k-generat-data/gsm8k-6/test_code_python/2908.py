def solution():
    total_earned = 400  # total amount earned
    cost_of_ingredients = 100  # cost of ingredients
    remaining_total = total_earned - cost_of_ingredients  # remaining amount after deducting cost of ingredients
    donated_to_homeless_shelter = (remaining_total/2) + 10  # half of remaining total plus $10 from Andrew's piggy bank
    result = donated_to_homeless_shelter
    return result

print(solution())