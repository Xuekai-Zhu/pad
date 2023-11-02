def solution():
    """
    Bill milked his cow and got 16 gallons of milk. He turned 1/4 into sour cream, 1/4 into butter, and kept the rest as whole milk.
    It takes 4 gallons of milk to make one gallon of butter and 2 gallons of milk to make 1 gallon of sour cream.
    If Bill sells butter for $5/gallon, sour cream for $6/gallon, and whole milk for $3/gallon, how much money does he make?
    """
    total_milk = 16
    butter_ratio = 1/4
    sour_cream_ratio = 1/4

    butter_produced = total_milk * butter_ratio / 4
    sour_cream_produced = total_milk * sour_cream_ratio / 2
    whole_milk_produced = total_milk - butter_produced - sour_cream_produced

    butter_sales = butter_produced * 5
    sour_cream_sales = sour_cream_produced * 6
    whole_milk_sales = whole_milk_produced * 3

    total_sales = butter_sales + sour_cream_sales + whole_milk_sales

    result = total_sales
    return result

print(solution())