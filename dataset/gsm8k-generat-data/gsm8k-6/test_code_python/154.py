def solution():
    # Find the amount of money Ariella has in her son's savings account
    ariella_money = 400 + 200  # Ariella has $200 more than Daniella
    ariella_interest = ariella_money * 0.1 * 2  # Simple interest earned by Ariella in 2 years
    ariella_total = ariella_money + ariella_interest  # Total amount Ariella will have after 2 years
    result = ariella_total
    return result

print(solution())