def solution():
    # Calculate the total number of crackers in 5 boxes
    total_crackers = 4 * 28 * 5

    # Calculate the number of peanut butter sandwiches Chad can make with the total number of crackers
    num_sandwiches = total_crackers // 2

    # Calculate the number of nights he can have 5 sandwiches
    num_nights = num_sandwiches // 5

    result = num_nights
    return result

print(solution())