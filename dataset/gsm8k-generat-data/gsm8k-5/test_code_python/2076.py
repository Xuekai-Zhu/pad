def solution():
    lightning_mcqueen_cost = 140000  # Lightning McQueen costs 140000$
    mater_cost = 0.1 * lightning_mcqueen_cost  # Mater costs 10% of what Lightning McQueen costs
    sally_mcqueen_cost = 3 * mater_cost  # Sally McQueen costs three times what Mater costs
    result = sally_mcqueen_cost
    return result

print(solution())