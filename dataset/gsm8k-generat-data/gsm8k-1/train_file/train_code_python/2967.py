def solution():
    """Jon makes 3/4's the salary that Karen makes. John makes $3000 per month. How long will it take him to make the same amount of money that Karen does in 3 months?"""
    john_salary = 3000
    karen_salary = john_salary / (3/4)
    karen_income = karen_salary * 3
    
    # calculate how many months John needs to make the same as Karen's 3 months
    months = karen_income / john_salary
    
    result = months
    return result

print(solution())