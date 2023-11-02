def solution():
    # Calculate the total monthly cost for each apartment, factoring in utilities and driving costs
    apartment1_cost = 800 + 260 + (31*20*0.58)  # cost of first apartment plus utilities plus driving costs
    apartment2_cost = 900 + 200 + (21*20*0.58)  # cost of second apartment plus utilities plus driving costs

    # Calculate the difference between the two apartment costs
    difference = round(apartment2_cost - apartment1_cost)

    result = difference
    return result

print(solution())