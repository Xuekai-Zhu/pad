def solution():
    """A local farmer is paying 4 kids to help plant rows of corn. Every row of corn contains 70 ears. A bag of corn seeds contains 48 seeds and you need 2 seeds per ear of corn. He pays the kids $1.5 per row. Afterward, the kids are so hungry that they end up spending half their money on dinner. The dinner cost $36 per kid. How many bags of corn seeds did each kid use?"""
    # Define the number of kids and the cost per row of corn
    num_kids = 4
    row_cost = 1.5

    # Define the number of ears of corn per row and the number of seeds needed per ear
    ears_per_row = 70
    seeds_per_ear = 2

    # Define the cost of dinner per kid
    dinner_cost_per_kid = 36

    # Calculate the total number of rows planted by the kids
    total_rows = num_kids * 10

    # Calculate the total cost for planting the rows
    total_cost = total_rows * row_cost

    # Calculate the cost of dinner for all the kids
    total_dinner_cost = num_kids * dinner_cost_per_kid

    # Calculate the profit for the kids
    total_profit = total_cost - (total_dinner_cost*2)

    # Calculate the total number of ears of corn planted
    total_ears = total_rows * ears_per_row

    # Calculate the total number of seeds needed
    total_seeds = total_ears * seeds_per_ear

    # Calculate the number of bags of corn seeds needed
    bags_of_seeds = total_seeds // 48

    # Calculate the number of bags each kid used
    bags_per_kid = bags_of_seeds // num_kids

    # Return the result
    result = bags_per_kid
    return result

print(solution())