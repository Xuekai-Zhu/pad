def solution():
    """James and Ali together own $250. If you know that James owns $40 more than Ali, then calculate the amount owned by James."""
    # Define the total amount owned
    total_amount = 250

    # Define the difference in amount owned between James and Ali
    difference = 40

    # Calculate the amount owned by Ali
    ali_amount = (total_amount - difference) / 2

    # Calculate the amount owned by James
    james_amount = ali_amount + difference

    # Display the amount owned by James
    result = james_amount
    return result

print(solution())