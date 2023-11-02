def solution():
    new_house_cost = 500000

    # Calculate the amount of the loan Tommy had to take for the new house
    loan_amount = 0.75 * new_house_cost

    # Calculate the amount Tommy paid for the 25% he didn't have to take as a loan
    paid_amount = new_house_cost - loan_amount

    # Calculate the value of Tommy's first house
    first_house_cost = paid_amount / 1.25
    result = first_house_cost
    return result

print(solution())