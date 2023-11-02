def solution():
    classmates = 35  # There are 35 people in Annie's class
    candies_per_classmate = 2  # Annie gave 2 candies to each classmate
    total_candies = classmates * candies_per_classmate + 12  # Annie had 12 candies left over

    # Calculate the total cost of the candy
    cost_per_candy = 0.1
    total_cost = total_candies * cost_per_candy
    result = total_cost
    return result

print(solution())