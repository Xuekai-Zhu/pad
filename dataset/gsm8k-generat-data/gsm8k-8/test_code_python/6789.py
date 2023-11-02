def solution():
    # Define the percentage of pay that is taxed
    tax_percentage = 0.1

    # Calculate the amount of tax
    tax = tax_percentage * 650

    # Calculate Jebb's take-home pay
    take_home_pay = 650 - tax
    result = take_home_pay
    return result

print(solution())