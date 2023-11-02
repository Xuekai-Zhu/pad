def solution():
    # Calculate the total amount of birdseed Leah has
    total_birdseed = 3 * 225 + 5 * 225  # 3 new boxes and 5 boxes already in the pantry

    # Calculate the total amount of birdseed the birds eat in a week
    total_birdseed_per_week = 100 + 50  # Parrot eats 100 grams and cockatiel eats 50 grams

    # Calculate the number of weeks Leah's birds can be fed with the current amount of birdseed
    weeks_of_supply = total_birdseed / total_birdseed_per_week
    result = weeks_of_supply
    return result

print(solution())