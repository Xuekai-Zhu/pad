def solution():
    # Define the amount earned for each survey
    survey_pay = 0.2*10
    
    # Calculate the total earnings for Monday and Tuesday
    monday_earnings = 3*survey_pay
    tuesday_earnings = 4*survey_pay
    
    # Calculate the total earnings for both days
    total_earnings = monday_earnings + tuesday_earnings
    result = total_earnings
    return result

print(solution())