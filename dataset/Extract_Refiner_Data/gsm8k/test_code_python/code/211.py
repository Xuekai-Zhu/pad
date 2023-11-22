def solution():
    
    # Define the cost of the shoes and the belt
    shoe_cost = 320
    belt_cost = 32

    # Calculate the total cost of the purchase
    total_cost = shoe_cost + belt_cost

    # Calculate the number of hours Lori needs to work to earn enough for the purchase
    hours_to_work = total_cost / 8

    # Display the number of hours
    result = hours_to_work
    return result

print(solution())