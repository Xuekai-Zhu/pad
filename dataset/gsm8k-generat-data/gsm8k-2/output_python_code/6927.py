def solution():
    """Kohen has a business selling apples. Once a week, he orders 10 boxes of apples to add to his stock. If each box has 300 apples and he sells 3/4 of his stock in a certain week, what total number of apples is not sold?"""
    boxes_per_week = 10
    apples_per_box = 300
    total_stock = boxes_per_week * apples_per_box
    sold_stock = 0.75 * total_stock
    unsold_stock = total_stock - sold_stock
    result = unsold_stock
    return result

print(solution())