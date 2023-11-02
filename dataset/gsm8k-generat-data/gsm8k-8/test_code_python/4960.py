def solution():
    # Define the prices of each dish
    dish1_price = 10
    dish2_price = 13
    dish3_price = 17

    # Calculate the total bill before tip
    total_bill = dish1_price + dish2_price + dish3_price

    # Calculate the amount of the tip
    tip = total_bill * 0.1

    # Calculate the total amount to be paid, including tip
    total_paid = total_bill + tip

    # Calculate the amount of gratuity, which is just the tip
    gratuity = tip
    result = gratuity
    return result

print(solution())