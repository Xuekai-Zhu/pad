def solution():
    """Sam earns $10 an hour on Math tutoring. For the first month, he earned $200; and for the second month, he earned $150 more than the first month. How many hours did he spend on tutoring for two months?"""
    # Define the earnings per hour and the earnings for the first month
    earnings_per_hour = 10
    first_month_earnings = 200

    # Calculate the earnings for the second month
    second_month_earnings = first_month_earnings + 150

    # Calculate the total earnings for two months
    total_earnings = first_month_earnings + second_month_earnings

    # Calculate the total number of hours spent on tutoring
    total_hours = total_earnings / earnings_per_hour

    result = total_hours
    return result

print(solution())