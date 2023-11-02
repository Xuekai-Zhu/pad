def solution():
    # Calculate the total amount of money Missy put in the bank over the 4 years
    total_amount = 450
    fourth_year = total_amount / 2
    third_year = fourth_year / 2
    second_year = third_year / 2
    first_year = total_amount - (fourth_year + third_year + second_year)

    result = first_year
    return result

print(solution())