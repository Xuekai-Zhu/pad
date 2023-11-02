def solution():
    num_people = 35
    candies_per_person = 2
    left_candies = 12
    candy_price = 0.1

    # Calculate the total number of candies Annie bought
    total_candies = num_people * candies_per_person - left_candies

    # Calculate the total cost of all candies Annie bought
    total_cost = total_candies * candy_price
    result = total_cost
    return result

print(solution())