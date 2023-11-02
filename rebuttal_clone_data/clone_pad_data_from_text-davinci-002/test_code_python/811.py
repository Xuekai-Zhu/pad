def solution():
    original_stock = 200
    fish_sold = 50
    fish_spoiled = ((original_stock - fish_sold) / 3)
    new_stock = 200
    total_stock = new_stock + (original_stock - fish_spoiled - fish_sold)
    result = total_stock
    return result

print(solution())