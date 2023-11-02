def solution():
    # Calculate the time it takes Danny to travel 200 miles for each sail
    time_24sqft = 200 / 50
    time_12sqft = 200 / 20

    # Calculate the difference in hours between the two sails
    time_difference = time_12sqft - time_24sqft
    result = time_difference
    return result

print(solution())