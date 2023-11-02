def solution():
    boys_percentage = 55  # 55% of Toby's friends are boys
    boys_count = 33  # Toby has 33 friends who are boys

    # Calculate the total number of friends
    total_friends = boys_count / (boys_percentage / 100)

    # Calculate the number of girls
    girls_count = total_friends - boys_count
    result = girls_count
    return result

print(solution())