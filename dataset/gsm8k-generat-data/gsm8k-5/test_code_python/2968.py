def solution():
    john_salary = 3000  # John makes $3000 per month
    karen_salary = john_salary / (3/4)  # Karen makes 4/3 times as much as John
    total_salary = karen_salary * 3  # Karen makes this amount in 3 months

    # Calculate the number of months it will take John to make the same amount as Karen in 3 months
    months = total_salary / john_salary
    result = months
    return result

print(solution())