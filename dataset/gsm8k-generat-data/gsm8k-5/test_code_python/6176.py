def solution():
    total_kids = 34  # There are 34 kids signed up in total
    boys = (total_kids - 22) / 2  # There are 22 more girls than boys
    girls = total_kids - boys  # Calculate the number of girls

    result = girls
    return result

print(solution())