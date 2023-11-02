def solution():
    """Randy has some money in his piggy bank. He spends 2 dollars every time he goes to the store. He makes 4 trips to the store every month. If he had $104 dollars left in his piggy bank after a year, how much money, in dollars, did he have at first?"""
    # Define the number of trips Randy makes to the store in a year
    TRIPS_PER_YEAR = 4 * 12

    # Define the amount Randy spends on each trip to the store
    SPENDING_PER_TRIP = 2

    # Calculate the total amount Randy spent over the course of a year
    total_spending = TRIPS_PER_YEAR * SPENDING_PER_TRIP

    # Calculate the amount Randy had left in his piggy bank after a year
    final_balance = 104

    # Calculate the amount Randy had at first
    initial_balance = final_balance + total_spending
    
    # Display the initial balance
    result = initial_balance
    return result

print(solution())