def solution():
    number_of_horses = 4  # Billy has 4 horses
    ounces_of_oats_per_day_per_horse = 8  # Each horse eats 4 pounds of oats, twice a day
    days = 3  # Billy wants to know how many pounds of oats he needs for 3 days

    # Calculate the total amount of oats required for all the horses for 3 days
    total_oats_required = number_of_horses * ounces_of_oats_per_day_per_horse * 16 * days # 16 ounces in a pound

    # Convert the amount of oats required to pounds
    pounds_of_oats_required = total_oats_required / 16
    result = pounds_of_oats_required
    return result

print(solution())