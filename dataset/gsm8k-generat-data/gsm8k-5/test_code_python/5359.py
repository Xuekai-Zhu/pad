def solution():
    cups_per_day = 12  # Cassie tries to drink at least 12 cups of water a day
    ounces_per_cup = 8  # There are 8 ounces of water in a cup
    ounces_per_bottle = 16  # Cassie's water bottle holds 16 ounces

    # Calculate the total number of ounces Cassie needs to drink per day
    total_ounces = cups_per_day * ounces_per_cup

    # Calculate the number of times Cassie needs to refill her water bottle a day
    refills_per_day = total_ounces / ounces_per_bottle
    result = refills_per_day
    return result

print(solution())