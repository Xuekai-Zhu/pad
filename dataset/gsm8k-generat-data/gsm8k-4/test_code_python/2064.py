def solution():
    """Your mom bought a refrigerator and a washing machine. Note that the price of the refrigerator is $4275 and the price of the washing machine is $1490 less than the price of the refrigerator. Calculate the total price of the purchases in dollars."""
    # Define the price of the refrigerator and calculate the price of the washing machine
    refrigerator_price = 4275
    washing_machine_price = refrigerator_price - 1490

    # Calculate the total price of the purchases
    total_price = refrigerator_price + washing_machine_price

    # Return the result
    result = total_price
    return result

print(solution())