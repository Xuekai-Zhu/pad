def solution():
    """Mildred and Candice went to the market. Mildred spent $25 while Candice spent $35. If their mom gave them $100 to spend, how much will be left with them after spending?"""
    # Define the initial amount of money given by mom
    initial_money = 100

    # Define the amount spent by Mildred and Candice
    mildred_spent = 25
    candice_spent = 35

    # Calculate the total amount spent
    total_spent = mildred_spent + candice_spent

    # Calculate the amount left with them after spending
    money_left = initial_money - total_spent

    # return the result
    result = money_left
    return result

print(solution())