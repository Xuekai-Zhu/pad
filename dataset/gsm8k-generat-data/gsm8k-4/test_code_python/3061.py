def solution():
    """Mikaela earns $10 an hour tutoring. For the first month, she tutored for 35 hours and in the second month, she tutored 5 hours more than the first month. She spent 4/5 of her total earnings on her personal needs and saved the rest of the money. How much did she save?"""
    # Define the hourly rate and the number of hours tutored in each month
    hourly_rate = 10
    month1_hours = 35
    month2_hours = month1_hours + 5

    # Calculate the total earnings for each month
    month1_earnings = hourly_rate * month1_hours
    month2_earnings = hourly_rate * month2_hours

    # Calculate the total earnings over the two months
    total_earnings = month1_earnings + month2_earnings

    # Calculate the amount spent on personal needs
    personal_needs = total_earnings * 4/5

    # Calculate the amount saved
    savings = total_earnings - personal_needs

    # return the result
    result = savings
    return result

print(solution())