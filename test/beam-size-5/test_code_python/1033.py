def solution():
    
    parmesan_price = 11
    mozzarella_price = 6
    parmesan_pounds = 2
    mozzarella_pounds = 3
    amor_pounds = parmesan_pounds + mozzarella_pounds
    total_cost = (parmesan_price * parmesan_pounds) + (mozzarella_price * mozzarella_pounds)
    money_left = 50 - total_cost
    result = money_left
    return result

print(solution())