def solution():
    """Bill milked his cow and got 16 gallons of milk. He turned 1/4 into sour cream, 1/4 into butter, and kept the rest as 
    whole milk. It takes 4 gallons of milk to make one gallon of butter and 2 gallons of milk to make 1 gallon of sour cream. 
    If Bill sells butter for $5/gallon, sour cream for $6/gallon, and whole milk for $3/gallon, how much money does he make?"""
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