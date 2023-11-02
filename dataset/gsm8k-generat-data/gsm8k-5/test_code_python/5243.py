def solution():
    book1_price = 5.5  # The price of the first book is 5.5£
    book2_price = 6.5  # The price of the second book is 6.5£
    total_cost = book1_price + book2_price  # The total cost of the books is 12£
    amount_paid = 20  # Sara gives the seller a 20£ bill

    # Calculate the change Sara gets back
    change = amount_paid - total_cost
    result = change
    return result

print(solution())