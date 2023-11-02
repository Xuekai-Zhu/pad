def solution():
    # Calculate the total amount Jill makes over three months
    first_month = 10 * 30
    second_month = (10 * 2) * 30
    third_month = ((10 * 2) * 2) * 15  # since Jill only works every other day
    total_amount = first_month + second_month + third_month
    result = total_amount
    return result

print(solution())