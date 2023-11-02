def solution():
    
    apple_price = 1
    orange_price = 2
    banana_price = 3
    total_fruits = 5 + 3 + 2
    total_price = (apple_price * 5) + (orange_price * 3) + (banana_price * 2)
    discount = (total_fruits // 5) * 1
    final_price = total_price - discount
    result = final_price
    return result

print(solution())