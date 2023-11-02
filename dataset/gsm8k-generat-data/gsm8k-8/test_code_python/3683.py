def solution():
    # Define total number of people and percentage of boys
    total_people = 50
    boys_percentage = 30

    # Calculate number of boys and girls
    boys_count = total_people * (boys_percentage / 100)
    girls_count = total_people - boys_count

    result = girls_count
    return result

print(solution())