def solution():
    january_amount = 19
    february_amount = january_amount
    total_amount = 46

    # Calculate the total amount saved in January and February
    jan_feb_total = january_amount + february_amount

    # Calculate the amount saved in March
    march_amount = total_amount - jan_feb_total
    result = march_amount
    return result

print(solution())