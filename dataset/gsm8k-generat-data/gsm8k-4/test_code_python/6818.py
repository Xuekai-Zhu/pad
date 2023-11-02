def solution():
    """1 chocolate bar costs $1.50 and can be broken into 3 sections to make 3 s'mores. Ron is hosting a boy scout camp out in his backyard for 15 scouts. He wants to make sure that there are enough chocolate bars for everyone to have 2 s'mores each. How much will he spend on chocolate bars?"""
    # Define the cost of one chocolate bar and the number of scouts
    chocolate_bar_cost = 1.5
    scouts = 15

    # Calculate the number of s'mores needed
    smores_needed = scouts * 2

    # Calculate the number of chocolate bars needed
    chocolate_bars_needed = smores_needed / 3

    # Calculate the total cost of the chocolate bars
    total_cost = chocolate_bars_needed * chocolate_bar_cost

    # Return the result as a float with 2 decimal points
    result = round(total_cost, 2)
    return result

print(solution())