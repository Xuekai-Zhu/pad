def solution():
    # Calculate the number of pencils she uses per day
    pencils_per_day = 10/5

    # Calculate the number of pencils she will use over 45 days
    pencils_over_45_days = pencils_per_day * 45

    # Calculate the number of 30-packs she will need to buy
    packs_needed = pencils_over_45_days/30

    # Calculate the total cost of the pencils
    cost = packs_needed * 4
    result = cost
    return result

print(solution())