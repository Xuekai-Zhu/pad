def solution():
    """The price of candy bars is twice the cost of caramel, and the cost of cotton candy is half the price of 4 candy bars. 
    If the price of 1 caramel is $3, how much do 6 candy bars, 3 caramel, and 1 cotton candy cost together?"""
    
    # Define the cost of caramel and calculate the cost of one candy bar
    caramel_cost = 3
    candy_bar_cost = 2 * caramel_cost
    
    # Calculate the price of 4 candy bars and the cost of one cotton candy
    four_candy_bars_price = 4 * candy_bar_cost
    cotton_candy_cost = four_candy_bars_price / 2
    
    # Calculate the total cost of 6 candy bars, 3 caramel, and 1 cotton candy
    total_cost = (6 * candy_bar_cost) + (3 * caramel_cost) + cotton_candy_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())