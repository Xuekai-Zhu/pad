def solution():
    
    # Define the initial number of candies sold and the number of candies he ordered
    initial_candies_sold = 150
    candies_ordered = 100

    # Calculate the total number of candies sold
    total_candies_sold = initial_candies_sold + candies_ordered

    # Calculate the remaining number of candies Dale needs to sell to reach his goal
    candies_remaining = 100 - total_candies_sold

    # Display the number of candies Dale still needs to sell
    result = candies_remaining
    return result

print(solution())