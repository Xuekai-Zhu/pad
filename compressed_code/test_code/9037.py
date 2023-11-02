def solution():
    
    first_month = 350
    second_month = (2 * first_month) + 50
    third_month = 4 * (first_month + second_month)
    total_amount = first_month + second_month + third_month
    result = total_amount
    return result

print(solution())