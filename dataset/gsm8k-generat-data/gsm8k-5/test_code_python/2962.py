def solution():
    # Calculate Hayden's earnings from driving
    hourly_wage = 15 * 8  # $15 per hour for 8 hours
    ride_bonus = 5 * 3  # $5 bonus for each of the 3 rides
    review_bonus = 20 * 2  # $20 bonus for 2 good reviews
    gas_reimbursement = 17 * 3  # $3 per gallon, 17 gallons

    total_earnings = hourly_wage + ride_bonus + review_bonus + gas_reimbursement
    result = total_earnings
    return result

print(solution())