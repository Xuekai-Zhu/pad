def solution():
    """Otto’s local kitchen supply store charges $5.00 for the first knife that you need sharpened. 
    They charge $4.00 for the next 3 knives and $3.00 for any knife after that. 
    If Otto has 9 knives that need to be sharpened, how much will it cost to sharpen his knives?"""
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