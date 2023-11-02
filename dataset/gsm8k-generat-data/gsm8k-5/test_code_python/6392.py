def solution():
    # Calculate the interest on the first bill
    interest_first_bill = 200 * 0.1 * 2  # $200 bill, 10% interest, 2 months overdue

    # Calculate the late fees on the second bill
    late_fees_second_bill = 50 * 6  # $50 fee per month, 6 months overdue

    # Calculate the late fees on the third bill
    late_fees_third_bill = 40 + (2*40)  # $40 fee for first month overdue, double for second month overdue

    # Calculate the total amount owed
    total_amount_owed = 200 + interest_first_bill + 130 + late_fees_second_bill + 444 + late_fees_third_bill
    result = total_amount_owed
    return result

print(solution())