def solution():
    mother_money = [50, 20, 20, 10, 10, 10]
    father_money = [50, 50, 50, 50, 20, 10]

    # Calculate the total amount of money Luke has
    total_money = sum(mother_money) + sum(father_money)

    # Calculate the school fee
    school_fee = total_money
    result = school_fee
    return result

print(solution())