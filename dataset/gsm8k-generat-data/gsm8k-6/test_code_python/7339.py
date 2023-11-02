def solution():
    # Calculate the total amount of milk produced
    total_milk = 12 * 4  # each cow produces 4 gallons of milk, and there are 12 cows

    # Calculate the total amount of milk sold
    milk_sold = 6 * 6  # each customer wants 6 gallons of milk, and there are 6 customers

    # Calculate the amount of milk turned into butter
    milk_to_butter = total_milk - milk_sold

    # Calculate the total amount earned from selling milk
    total_milk_earned = milk_sold * 3

    # Calculate the total amount earned from selling butter
    total_butter_earned = (milk_to_butter / 2) * 3  # 1 gallon of milk produces 2 sticks of butter
    total_butter_earned += (milk_to_butter / 2) * 1.5  # each stick of butter sells for $1.5

    # Calculate the total amount earned
    total_earned = total_milk_earned + total_butter_earned
    result = total_earned
    return result

print(solution())