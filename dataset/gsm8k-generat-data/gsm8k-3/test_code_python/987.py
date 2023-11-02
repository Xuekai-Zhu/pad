def solution():
    """If Lucy would give Linda $5, Lucy would have the same amount of money as Linda. If Lucy originally had $20, how much money did Linda have at the beginning?"""
    # Define the original amount of money Lucy had and the amount she will give to Linda
    lucy_money = 20
    linda_money = 0

    # Calculate the amount of money Linda had at the beginning
    linda_money = lucy_money - 5

    # Display the amount of money Linda had at the beginning
    result = linda_money
    return result

print(solution())