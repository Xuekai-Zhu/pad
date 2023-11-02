def solution():
    original_milk_price = 3.0
    discounted_milk_price = 2.0
    milk_discount = original_milk_price - discounted_milk_price

    cereal_discount = 1.0
    num_milk_gallons = 3
    num_cereal_boxes = 5

    # Calculate the total savings from the milk discount
    milk_savings = num_milk_gallons * milk_discount

    # Calculate the total savings from the cereal discount
    cereal_savings = num_cereal_boxes * cereal_discount

    # Calculate the total savings from both discounts
    total_savings = milk_savings + cereal_savings
    result = total_savings
    return result

print(solution())