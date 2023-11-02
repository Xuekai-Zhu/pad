def solution():
    daniella_money = 400  # Daniella has $400 in her son's savings account
    ariella_money = daniella_money + 200  # Ariella has $200 more than Daniella in her son's savings account
    rate_of_interest = 0.1  # Ariella's account earns her simple interest at the rate of 10% per annum
    time = 2  # Ariella wants to know how much money she will have after two years

    # Calculate the amount of money Ariella will have after two years
    ariella_money_after_two_years = ariella_money + (ariella_money * rate_of_interest * time)

    result = ariella_money_after_two_years
    return result

print(solution())