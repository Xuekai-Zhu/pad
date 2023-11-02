def solution():
    heaven_cost = 2*5 + 4*5  # Heaven spent $5 for each sharpener and notebook
    brother_remaining = 100 - heaven_cost  # Calculate the remaining amount after Heaven's purchase
    erasers_cost = 10*4  # Her younger brother spent $4 for each of the ten erasers
    highlighters_cost = brother_remaining - erasers_cost  # Calculate the cost of highlighters

    result = highlighters_cost
    return result

print(solution())