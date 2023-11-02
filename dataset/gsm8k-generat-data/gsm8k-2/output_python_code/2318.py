def solution():
    """Mr. Mayer bought Corgi dogs for $1000 each. He plans to sell them with a 30% profit. If one of his friends wants to buy two dogs, how much should his friend pay?"""
    dog_price = 1000
    profit_margin = 0.3
    selling_price = dog_price + (dog_price * profit_margin)
    friend_dogs = 2
    total_price = selling_price * friend_dogs
    result = total_price
    return result

print(solution())