def solution():
    """Susan is picking strawberries. She's trying to fill her basket, but out of every handful of 5 strawberries she can't help but eat one of them herself. If her basket holds 60 strawberries, how many berries will she actually pick before she fills it?"""
    # Define the number of strawberries eaten in each handful
    eaten_per_handful = 1

    # Define the number of strawberries in each full handful
    full_handful = 5

    # Calculate the number of non-full handfuls Susan needs to pick to fill her basket
    non_full_handfuls = (60 - eaten_per_handful) // full_handful

    # Calculate the total number of strawberries Susan needs to pick
    total_strawberries = (non_full_handfuls + 1) * full_handful + eaten_per_handful

    # Return the result
    result = total_strawberries
    return result

print(solution())