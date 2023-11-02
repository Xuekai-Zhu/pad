def solution():
    boys_percentage = 0.55
    num_boys = 33

    # Calculate the total number of friends Toby has
    total_friends = num_boys / boys_percentage

    # Calculate the number of girls Toby has as friends
    num_girls = total_friends - num_boys
    result = num_girls
    return result

print(solution())