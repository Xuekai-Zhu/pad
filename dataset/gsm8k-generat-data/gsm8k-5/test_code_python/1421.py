def solution():
    total_plates_needed = 84  # Xavier needs 84 plates in total
    plates_already_owned = 21 + 28  # Xavier already has 21 green plates and 28 red plates
    plates_to_buy = total_plates_needed - plates_already_owned  # Xavier needs to buy the remaining plates
    result = plates_to_buy
    return result

print(solution())