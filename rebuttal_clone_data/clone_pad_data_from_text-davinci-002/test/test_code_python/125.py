def solution():
    
    cost_of_bread = 4.2
    cost_of_cheese = 2.05
    money_given = 7.0
    money_owed = cost_of_bread + cost_of_cheese
    change_due = money_given - money_owed
    quarter = 0.25
    dime = 0.1
    nickel = 0.05
    num_quarters = 1
    num_dimes = 1
    num_nickels = (change_due - (quarter * num_quarters) - (dime * num_dimes)) / nickel
    result = num_nickels
    return result

print(solution())