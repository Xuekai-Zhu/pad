def solution():
    # Calculate the total amount of birdseed Leah has
    total_birdseed = 3 * 225 + 5 * 225  # 3 new boxes and 5 old boxes

    # Calculate the total amount of birdseed her birds eat per week
    total_birdseed_per_week = 100 + 50  # parrot eats 100 grams and cockatiel eats 50 grams per week

    # Calculate the number of weeks Leah can feed her birds with the birdseed she has
    weeks_of_food = total_birdseed // total_birdseed_per_week

    result = weeks_of_food
    return result

print(solution())