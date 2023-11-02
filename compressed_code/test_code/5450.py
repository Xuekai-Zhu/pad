def solution():
    
    first_knife_price = 5
    second_to_fourth_knife_price = 4
    fifth_and_above_knife_price = 3
    total_price = first_knife_price
    
    for i in range(2, 10):
        if i <= 4:
            total_price += second_to_fourth_knife_price
        else:
            total_price += fifth_and_above_knife_price

    result = total_price
    return result

print(solution())