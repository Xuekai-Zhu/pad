def solution():
    # Calculate the amount of milk turned into sour cream
    sour_cream_milk = 16 * (1/4)
    sour_cream = sour_cream_milk / 2  # 2 gallons of milk make 1 gallon of sour cream

    # Calculate the amount of milk turned into butter
    butter_milk = 16 * (1/4)
    butter = butter_milk / 4  # 4 gallons of milk make 1 gallon of butter

    # Calculate the amount of milk kept as whole milk
    whole_milk = 16 - sour_cream_milk - butter_milk

    # Calculate the total amount of money made from selling butter
    butter_money = butter * 5

    # Calculate the total amount of money made from selling sour cream
    sour_cream_money = sour_cream * 6

    # Calculate the total amount of money made from selling whole milk
    whole_milk_money = whole_milk * 3

    # Calculate the total amount of money made
    total_money = butter_money + sour_cream_money + whole_milk_money
    result = total_money
    return result

print(solution())