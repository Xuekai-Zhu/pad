def solution():
    # Calculate the balance after 3 years of compounded interest
    balance = 10000 * (1 + 0.2)**3  

    # Calculate the additional amount invested to triple the original investment
    additional_investment = balance * 2/3  

    # Calculate the total balance after the additional investment
    total_balance = balance + additional_investment  

    # Calculate the balance after a year of 15% return
    final_balance = total_balance * 1.15  

    result = final_balance
    return result

print(solution())