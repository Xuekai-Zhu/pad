def solution():
    """Kohen has a business selling apples. Once a week, he orders 10 boxes of apples to add to his stock. If each box has 300 apples and he sells 3/4 of his stock in a certain week, what total number of apples is not sold?"""
    # Define the number of boxes ordered and the number of apples per box
    boxes_ordered = 10
    apples_per_box = 300

    # Calculate the total number of apples in the order
    total_apples = boxes_ordered * apples_per_box

    # Calculate the number of apples sold
    apples_sold = total_apples * 0.75

    # Calculate the number of apples left unsold
    apples_not_sold = total_apples - apples_sold

    result = apples_not_sold
    return result

print(solution())