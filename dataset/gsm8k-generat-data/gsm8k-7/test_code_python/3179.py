def solution():
    laptop_price = 600
    smartphone_price = 400
    num_laptops = 2
    num_smartphones = 4
    total_price = (num_laptops * laptop_price) + (num_smartphones * smartphone_price)
    change = 3000 - total_price
    result = change
    return result

print(solution())