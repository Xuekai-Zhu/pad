def solution():
    hours_worked = [10, 8, 15]  # Hours worked on the first, second and third day respectively
    pay_rate = 10  # Each man is paid $10 per hour of work

    # Calculate the total hours worked by the two men
    total_hours = sum(hours_worked)
    
    # Calculate the total amount of money each man received
    total_pay = total_hours * pay_rate
    
    # Calculate the total amount of money both men received altogether
    total_pay_both = total_pay * 2
    result = total_pay_both
    return result

print(solution())