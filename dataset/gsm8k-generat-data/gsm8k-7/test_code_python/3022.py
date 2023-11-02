def solution():
    new_house_cost = 500000
    percent_increase = 0.25
    loan_percent = 0.75

    # Calculate the amount Tommy paid for his old house before the 25% increase in value
    old_house_cost = new_house_cost / (1 + percent_increase)

    # Calculate the amount Tommy had to take a loan for
    loan_amount = new_house_cost * loan_percent

    # Calculate the amount Tommy paid for the 25% he could afford
    paid_amount = new_house_cost - loan_amount

    # Calculate the amount Tommy paid for his old house
    old_house_paid = paid_amount - (paid_amount * percent_increase)

    result = old_house_paid
    return result

print(solution())