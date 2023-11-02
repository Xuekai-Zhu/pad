def solution():
    iPhone_price = 800
    iPhone_discount = 15
    iWatch_price = 300
    iWatch_discount = 10
    cashback_discount = 2
    total_iPhone_price = iPhone_price - (iPhone_price * (iPhone_discount / 100))
    total_iWatch_price = iWatch_price - (iWatch_price * (iWatch_discount / 100))
    total_price = total_iPhone_price + total_iWatch_price
    final_price = total_price - (total_price * (cashback_discount / 100))
    result = final_price
    return result

print(solution())