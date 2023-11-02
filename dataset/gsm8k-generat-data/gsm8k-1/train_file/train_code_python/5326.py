def solution():
    """Calculate the total price a buyer who takes two pieces of jewelry and five paintings would pay"""
    original_jewelry_price = 30
    increased_jewelry_price = original_jewelry_price + 10
    original_painting_price = 100
    increased_painting_price = original_painting_price * 1.2
    num_jewelry = 2
    num_paintings = 5
    total_price = (num_jewelry * increased_jewelry_price) + (num_paintings * increased_painting_price)
    result = total_price
    return result

print(solution())