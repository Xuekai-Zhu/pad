def solution():
    new_house_cost = 500000  # Tommy buys a new house for $500,000
    loan_percent = 0.75  # Tommy takes a loan for 75% of the cost of the new house
    loan_amount = loan_percent * new_house_cost  # Tommy takes a loan for this amount
    old_house_cost = loan_amount / 1.25  # Tommy's old house was worth 25% less than what he sold it for

    result = old_house_cost
    return result

print(solution())