def solution():
    regular_large_price =  # Enter the price of a regular large pizza
    medium_price =  # Enter the price of a regular medium pizza
    promotion_price = 5  # The promotion price for each medium pizza is $5

    # Calculate the savings from buying the regular large pizza
    savings_large = medium_price * 3 - promotion_price * 3

    # Calculate the savings from buying the 3 medium pizzas
    savings_medium = (medium_price * 3) - (promotion_price * 3)

    # Calculate the total savings
    total_savings = savings_large + savings_medium
    result = total_savings
    return result

print(solution())