def solution():
    strawberries_needed = 60
    strawberries_eaten_per_handful = 1
    strawberries_per_handful = 5

    # Calculate the total number of strawberries Susan needs to pick
    total_strawberries = strawberries_needed / (1 - (strawberries_eaten_per_handful / strawberries_per_handful))

    # Round up to the nearest whole number
    total_strawberries = int(total_strawberries) + 1

    result = total_strawberries
    return result

print(solution())