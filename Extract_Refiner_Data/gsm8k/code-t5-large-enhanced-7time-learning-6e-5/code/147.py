def solution():
    
    # Define the cost to inflate each tire
    TIRE_COST = 0.25

    # Define the number of people who came by each tire
    bicycles = 5
    tricycles = 3
    unicycles = 1

    # Calculate the total cost of inflating both tires
    total_cost = (bicycles * TIRE_COST) + (tricycles * TIRE_COST) + (unicycles * TIRE_COST)

    # Display the total cost
    result = total_cost
    return result

print(solution())