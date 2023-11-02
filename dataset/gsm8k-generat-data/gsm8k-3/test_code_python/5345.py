def solution():
    """Lee wants to propose marriage to Sierra. He wants to follow the adage that you should spend two months' salary on the ring. He earns $60,000 per year in salary and can save $1000 per month. How long will it take before he can propose to Sierra?"""
    # Define the amount Lee can save per month
    savings_per_month = 1000

    # Define the number of months' salary Lee wants to spend on the ring
    months_salary = 2

    # Calculate Lee's monthly salary
    monthly_salary = 60000 / 12

    # Calculate the cost of the ring based on Lee's salary
    ring_cost = months_salary * monthly_salary

    # Calculate the number of months it will take Lee to save up for the ring
    months_to_save = ring_cost / savings_per_month

    # Display the number of months it will take to save up
    result = months_to_save
    return result

print(solution())