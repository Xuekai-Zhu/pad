def solution():
    total_people = 50
    boys_percent = 0.3  # 30% of the people are boys

    # Calculate the number of boys at the party
    num_boys = total_people * boys_percent

    # Calculate the number of girls at the party
    num_girls = total_people - num_boys
    result = num_girls
    return result

print(solution())