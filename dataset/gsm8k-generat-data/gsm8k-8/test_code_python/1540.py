def solution():
    # Calculate the total amount after 3 years of initial investment
    initial_amount = 10000
    interest_rate = 0.20
    years = 3
    final_amount = initial_amount * (1 + interest_rate)**years

    # Calculate the additional investment needed to reach three times as much
    additional_investment = final_amount * 2

    # Calculate the total amount after the additional investment
    total_investment = initial_amount + additional_investment
    total_return = total_investment * 0.15
    total_amount = total_investment + total_return
    result = total_amount
    return result

print(solution())