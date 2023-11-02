def solution():
    
    dog_price = 1000
    profit_margin = 0.3
    selling_price = dog_price + (dog_price * profit_margin)
    friend_dogs = 2
    total_price = selling_price * friend_dogs
    result = total_price
    return result

print(solution())