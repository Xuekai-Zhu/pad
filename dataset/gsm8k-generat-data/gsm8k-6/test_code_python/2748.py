def solution():
    # Calculate the final price of the book after the decrease and increase
    original_price = 400
    decreased_price = original_price * 0.85  # 15% decrease
    increased_price = decreased_price * 1.4  # 40% increase
    result = increased_price
    return result

print(solution())