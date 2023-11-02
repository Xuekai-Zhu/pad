def solution():
    boxes_per_week = 10  # Kohen orders 10 boxes of apples per week
    apples_per_box = 300  # Each box contains 300 apples
    total_stock = boxes_per_week * apples_per_box  # Kohen's total stock of apples
    sold_stock = 0.75 * total_stock  # Kohen sells 3/4 of his stock in a week
    unsold_stock = total_stock - sold_stock  # Calculate the number of apples that are not sold
    result = unsold_stock
    return result

print(solution())