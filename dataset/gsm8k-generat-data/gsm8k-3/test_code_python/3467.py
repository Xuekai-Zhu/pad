def solution():
    """George is about to celebrate his 25th birthday. Since his 15th birthday, he's been given a special $1 bill from his parents. They told him that on his 25th birthday, for every bill he still has, they will give him $1.5 in exchange. He spent 20% of his special bills. How much will he receive from his parents when he exchanges them?"""
    # Define the starting number of special bills
    starting_bills = 25

    # Calculate the number of bills George still has
    bills_remaining = starting_bills - (starting_bills * 0.2)

    # Calculate the amount George will receive from his parents
    amount_received = bills_remaining * 1.5

    # Display the amount received
    result = amount_received
    return result

print(solution())