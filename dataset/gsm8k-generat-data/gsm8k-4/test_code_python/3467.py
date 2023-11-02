def solution():
    """George is about to celebrate his 25th birthday. Since his 15th birthday, he's been given a special $1 bill from his parents. They told him that on his 25th birthday, for every bill he still has, they will give him $1.5 in exchange. He spent 20% of his special bills. How much will he receive from his parents when he exchanges them?"""
    # Define the number of special bills George received
    bills_received = 25 - 15 + 1

    # Calculate the number of bills George spent
    bills_spent = round(bills_received * 0.2)

    # Calculate the number of bills George will exchange with his parents
    bills_remaining = bills_received - bills_spent

    # Calculate the amount of money George will receive from his parents
    money_received = bills_remaining * 1.5

    # return the result
    result = money_received
    return result

print(solution())