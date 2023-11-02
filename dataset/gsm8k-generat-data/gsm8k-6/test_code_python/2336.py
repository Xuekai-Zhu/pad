def solution():
    # Calculate Latia's monthly earnings
    monthly_earnings = 10 * 30

    # Calculate the number of months it will take to earn $1700
    num_months = 1700 // monthly_earnings

    # Calculate the number of hours Latia needs to work to earn the remaining amount
    remaining_earnings = 1700 % monthly_earnings
    hours_needed = remaining_earnings / 10

    result = hours_needed
    return result

print(solution())