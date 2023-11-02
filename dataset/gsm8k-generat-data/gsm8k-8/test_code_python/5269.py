def solution():
    # Calculate the total amount of money Luke has
    luke_money = 50 + 2*20 + 3*10 + 4*50 + 20 + 10

    # Calculate the total amount given by Luke's parents
    parent_money = 4*50 + 20 + 10

    # Calculate the school fee
    school_fee = parent_money - luke_money
    result = school_fee
    return result

print(solution())