def solution():
    milk_price = 3
    milk_discounted_price = 2
    cereal_discount = 1

    milk_savings = (milk_price - milk_discounted_price) * 3
    cereal_savings = cereal_discount * 5
    total_savings = milk_savings + cereal_savings
    result = total_savings
    return result

print(solution())