def solution():
    # Define Reginald's bike cost and the cost of repairs
    bike_cost = 80
    repair_cost = bike_cost * 0.25

    # Calculate Reginald's total expenses
    total_expenses = bike_cost + repair_cost

    # Define the fraction of money he has left after paying for repairs
    fraction_left = 1/5

    # Calculate how much money he made before paying for repairs
    money_before_repairs = total_expenses / (1 - fraction_left)

    # Calculate how many apples he sold
    apples_sold = money_before_repairs / 1.25
    result = apples_sold
    return result

print(solution())