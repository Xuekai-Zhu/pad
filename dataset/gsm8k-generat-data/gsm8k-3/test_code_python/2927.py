def solution():
    """A shoe company sells $4000 worth of shoes every month. If they want to make $60000 in an entire year how many more dollars per month should they make selling shoes?"""
    # Define the current monthly sales and the desired annual profit
    current_sales = 4000
    desired_profit = 60000

    # Calculate the total annual sales needed to achieve the desired profit
    total_sales = desired_profit + (current_sales * 12)

    # Calculate the additional monthly sales needed to achieve the total sales goal
    additional_sales = (total_sales / 12) - current_sales

    # Display the additional monthly sales needed
    result = additional_sales
    return result

print(solution())