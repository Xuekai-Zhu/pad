def solution():
    
    # Define the cost of each item
    LOLLIPOP_PRICE = 0.40
    CANDY_PRICE = 3.20

    # Define the number of each item purchased
    num_lollipops = 5
    num_candies = 4

    # Calculate the total cost of the lollipops
    lollipop_cost = num_lollipops * LOLLIPOP_PRICE

    # Calculate the total cost of the candies
    candy_cost = num_candies * CANDY_PRICE

    # Calculate the total cost of 10 lollipops and 10 candies
    total_cost = (10 * lollipop_cost) + (10 * candy_cost)

    # Display the total cost
    result = total_cost
    return result

print(solution())