def solution():
    # Calculate the total amount of oats needed to feed Billy's horses for 3 days
    oats_per_horse_per_day = 4 * 2  # each horse eats 4 pounds of oats twice a day
    total_oats_needed = oats_per_horse_per_day * 4 * 3  # Billy has 4 horses and needs to feed them for 3 days
    result = total_oats_needed
    return result

print(solution())