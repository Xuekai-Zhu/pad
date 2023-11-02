def solution():
    milk_price = 3  # Original price of a gallon of whole milk
    milk_discounted_price = 2  # Discounted price of a gallon of whole milk
    cereal_discount = 1  # Discount on a box of cereal

    # Calculate the amount saved on milk purchases
    milk_saved = (milk_price - milk_discounted_price) * 3  # Three gallons of milk purchased

    # Calculate the amount saved on cereal purchases
    cereal_saved = cereal_discount * 5  # Five boxes of cereal purchased

    # Total amount saved via discounts
    total_saved = milk_saved + cereal_saved
    result = total_saved
    return result

print(solution())