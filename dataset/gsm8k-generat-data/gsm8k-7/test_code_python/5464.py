def solution():
    total_milk = 16

    # Calculate the amount of milk turned into butter
    butter_milk = total_milk / 4
    butter_gallons = butter_milk / 4
    butter_income = butter_gallons * 5

    # Calculate the amount of milk turned into sour cream
    sour_cream_milk = total_milk / 4
    sour_cream_gallons = sour_cream_milk / 2
    sour_cream_income = sour_cream_gallons * 6

    # Calculate the amount of whole milk left
    whole_milk_gallons = total_milk - (butter_gallons + sour_cream_gallons)
    whole_milk_income = whole_milk_gallons * 3

    # Calculate total income
    total_income = butter_income + sour_cream_income + whole_milk_income
    result = total_income
    return result

print(solution())