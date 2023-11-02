def solution():
    """Marly has ten $20 bills, eight $10 bills, and four $5 bills. If she wants to change her bills to $100 bills, how many pieces of $100 bills will she have?"""
    # Define the value of each bill
    TWENTY_VALUE = 20
    TEN_VALUE = 10
    FIVE_VALUE = 5
    HUNDRED_VALUE = 100

    # Define the number of each type of bill Marly has
    twenty_count = 10
    ten_count = 8
    five_count = 4

    # Calculate the total value of Marly's bills
    total_value = (twenty_count * TWENTY_VALUE) + (ten_count * TEN_VALUE) + (five_count * FIVE_VALUE)

    # Calculate the number of $100 bills Marly can get
    hundred_count = total_value // HUNDRED_VALUE

    # Display the number of $100 bills Marly will have
    result = hundred_count
    return result

print(solution())