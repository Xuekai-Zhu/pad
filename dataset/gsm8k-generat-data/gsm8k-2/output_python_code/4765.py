def solution():
    """A swarm of ants discovered a pile of sugar that spilled from a dropped bag. They begin to harvest it and carry it off to their anthill. Every hour, the ants remove 4 ounces of sugar. The bag of sugar held 24 ounces before it was dropped. After three hours, how many more hours will the ants need to harvest the remaining sugar?"""
    initial_sugar = 24
    sugar_per_hour = 4
    harvested_sugar = sugar_per_hour * 3
    remaining_sugar = initial_sugar - harvested_sugar
    additional_hours_needed = remaining_sugar / sugar_per_hour
    result = additional_hours_needed
    return result

print(solution())