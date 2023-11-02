def solution():
    """Luke pays a school fee. His mother gave him one $50 bill, two $20 bills, and three $10 bills. His father gave him four $50 bills, one $20 bill, and one $10 bill. If his parents gave him the exact amount for the school fee, how much is the school fee?"""
    # Define the value of each type of bill
    BILL_50 = 50
    BILL_20 = 20
    BILL_10 = 10

    # Calculate the total amount of money given by Luke's mother
    mother_total = (1 * BILL_50) + (2 * BILL_20) + (3 * BILL_10)

    # Calculate the total amount of money given by Luke's father
    father_total = (4 * BILL_50) + (1 * BILL_20) + (1 * BILL_10)

    # Calculate the total amount of money given for the school fee
    total = mother_total + father_total

    # Display the total amount
    result = total
    return result

print(solution())