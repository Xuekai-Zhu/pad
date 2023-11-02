def solution():
    
    total_milk = 16
    sour_cream_amount = total_milk * (1/4)
    butter_amount = total_milk * (1/4)
    whole_milk_amount = total_milk - sour_cream_amount - butter_amount
    butter_price = 5
    sour_cream_price = 6
    whole_milk_price = 3
    butter_gallons = butter_amount / 4
    sour_cream_gallons = sour_cream_amount / 2
    whole_milk_gallons = whole_milk_amount
    total_earnings = (butter_gallons * butter_price) + (sour_cream_gallons * sour_cream_price) + (whole_milk_gallons * whole_milk_price)
    result = total_earnings
    return result

print(solution())