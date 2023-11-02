def solution():
    amount_paid = 15000  # Venny spent $15000 on the used car
    percentage_of_original_price = 40  # The used car cost 40% of the original price

    # Calculate the original price of the car
    original_price = (100/percentage_of_original_price) * amount_paid
    result = original_price
    return result

print(solution())