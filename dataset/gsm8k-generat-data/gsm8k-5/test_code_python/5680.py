def solution():
    pay = 500  # Jonessa's pay is $500
    tax_percentage = 0.1  # Ten percent of her pay goes to tax

    # Calculate the amount of tax Jonessa has to pay
    tax = pay * tax_percentage

    # Calculate Jonessa's take-home pay
    take_home_pay = pay - tax
    result = take_home_pay
    return result

print(solution())