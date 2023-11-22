def solution():
    
    # Define the initial amount of money
    initial_money = 40

    # Define the amount of money given by the father
    father_money = 100

    # Define the cost of the jeans and the bag
    jeans_cost = 2 * 30
    bag_cost = 20

    # Calculate the total cost of the purchase
    total_cost = jeans_cost + bag_cost

    # Calculate the remaining money
    remaining_money = initial_money + father_money - total_cost

    # return the result
    result = remaining_money
    return result

print(solution())