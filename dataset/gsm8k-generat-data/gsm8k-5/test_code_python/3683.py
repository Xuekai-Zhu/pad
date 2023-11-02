def solution():
    total_people = 50  # The total number of people at the party is 50
    boys_percentage = 30  # 30% of them are boys

    # Calculate the number of boys at the party
    boys = (boys_percentage / 100) * total_people

    # Calculate the number of girls at the party
    girls = total_people - boys
    result = girls
    return result

print(solution())