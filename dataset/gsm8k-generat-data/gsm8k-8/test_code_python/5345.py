def solution():
    # Calculate Lee's monthly salary
    monthly_salary = 60000 / 12

    # Calculate Lee's savings per month
    savings_per_month = 1000

    # Calculate the amount Lee can spend on the ring
    ring_budget = 2 * monthly_salary

    # Calculate the number of months it will take to save up for the ring
    months_to_save = ring_budget / savings_per_month

    result = months_to_save
    return result

print(solution())