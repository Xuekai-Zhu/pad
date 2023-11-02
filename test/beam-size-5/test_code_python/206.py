def solution():
    
    # Define the cost of the jacket and shoes
    jacket_cost = 30
    shoes_cost = 20

    # Calculate the total cost of the jacket and shoes
    total_cost = jacket_cost + (2 * shoes_cost)

    # Calculate how much Sara earned from babysitting the neighbor's kids
    babysitting_earnings = 4 * 4

    # Calculate how much Sara still needs to mow the lawn
    lawn_cost = total_cost - babysitting_earnings - 10

    # Calculate how many times Sara needs to mow the lawn
    mows_needed = lawn_cost / 4

    # Display the number of times Sara needs to mow the lawn
    result = mows_needed
    return result

print(solution())