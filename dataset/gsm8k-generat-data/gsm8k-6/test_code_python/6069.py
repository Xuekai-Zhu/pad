def solution():
    # Calculate the total number of eggs decorated per hour when Mia and Billy work together
    eggs_per_hour = (2 * 12) + 10  # 2 dozen eggs per hour for Mia and 10 eggs per hour for Billy

    # Calculate the total hours required to decorate 170 eggs
    total_hours = 170 / eggs_per_hour

    result = total_hours
    return result

print(solution())