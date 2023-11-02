def solution():
    """Thomas started saving for a car almost 2 years ago. For the first year, his weekly allowance was $50. In the second year, he got a job that pays $9 an hour at a coffee shop and worked 30 hours a week, so his parents discontinued his allowance. If the car he wants to buy is $15,000 and he spends $35 a week on himself, how much more money does Thomas need to buy the car by the end of the 2 years?"""
    # Define the car cost, allowance and expenses
    CAR_COST = 15000
    ALLOWANCE_FIRST_YEAR = 50
    EXPENSES = 35

    # Calculate savings from the first year
    savings_first_year = ALLOWANCE_FIRST_YEAR * 52

    # Calculate savings from the second year
    job_pay = 9 * 30
    job_weekly = job_pay - EXPENSES
    savings_second_year = job_weekly * 52

    # Calculate total savings
    total_savings = savings_first_year + savings_second_year

    # Calculate how much more money Thomas needs to buy the car
    needed_money = CAR_COST - total_savings

    # Display how much more money Thomas needs
    result = needed_money
    return result

print(solution())