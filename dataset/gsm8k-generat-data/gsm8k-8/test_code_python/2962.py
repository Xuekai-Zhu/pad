def solution():
    # Calculate Hayden's earnings from driving
    hourly_earnings = 15 * 8
    ride_earnings = 5 * 3
    total_earnings = hourly_earnings + ride_earnings

    # Calculate Hayden's bonus from good reviews
    review_bonus = 20 * 2

    # Calculate Hayden's reimbursement for gas
    gas_reimbursement = 17 * 3

    # Calculate Hayden's total earnings for the day
    total_earnings += review_bonus + gas_reimbursement

    result = total_earnings
    return result

print(solution())