def solution():
    """The selling price of a bicycle that had sold for $220 last year was increased by 15%. What is the new price?"""
    # Define the original selling price and the percentage increase
    original_price = 220
    increase_percent = 15

    # Calculate the amount of increase
    increase_amount = original_price * (increase_percent / 100)

    # Calculate the new selling price
    new_price = original_price + increase_amount

    # Display the new selling price
    result = new_price
    return result

print(solution())