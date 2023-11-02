def solution():
    annual_profits = 8000
    q1_profits = 1500
    q3_profits = 3000
    q4_profits = 2000

    # Calculate the total profits from the first three quarters
    total_q1_q3_q4 = q1_profits + q3_profits + q4_profits

    # Calculate the profits from the second quarter
    q2_profits = annual_profits - total_q1_q3_q4
    result = q2_profits
    return result

print(solution())