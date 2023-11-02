def solution():
    john_salary = 3000 # salary of John
    karen_salary = (4/3) * john_salary # salary of Karen
    total_salary = karen_salary * 3 # total salary Karen makes in 3 months
    months_to_equal = total_salary / john_salary # months it takes for John to make same amount as Karen in 3 months
    result = months_to_equal
    return result

print(solution())