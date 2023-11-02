def solution():
    """The dinner bill for 6 friends came to $150. Silas said he would pay for half of the bill and the remaining friends could split the rest of the bill and leave a 10% tip for the whole meal. How many dollars will one of the friends pay?"""
    # Define the number of friends and the total bill
    NUM_FRIENDS = 6
    TOTAL_BILL = 150

    # Calculate Silas' contribution
    silas_contribution = TOTAL_BILL / 2

    # Calculate the remaining bill after Silas' contribution
    remaining_bill = TOTAL_BILL - silas_contribution

    # Calculate the total bill with the 10% tip
    total_with_tip = remaining_bill * 1.1

    # Calculate the amount each friend will pay
    amount_per_friend = total_with_tip / (NUM_FRIENDS - 1)

    # Display the amount one friend will pay
    result = amount_per_friend
    return result

print(solution())