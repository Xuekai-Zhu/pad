def solution():
    """Susan is picking strawberries. She's trying to fill her basket, but out of every handful of 5 strawberries she can't help but eat one of them herself. If her basket holds 60 strawberries, how many berries will she actually pick before she fills it?"""
    # Calculate the number of strawberries Susan needs to pick to fill her basket
    strawberries_needed = 60

    # Calculate the number of strawberries Susan eats in each handful
    eaten_per_handful = 1

    # Calculate the number of strawberries in each handful before Susan eats one
    total_per_handful = 5

    # Calculate the number of strawberries Susan picks before she fills her basket
    total_picked = (strawberries_needed / (total_per_handful - eaten_per_handful)) * total_per_handful

    # Display the total number of strawberries Susan picked
    result = total_picked
    return result

print(solution())