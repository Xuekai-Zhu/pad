def solution():
    """Kohen has a business selling apples. Once a week, he orders 10 boxes of apples to add to his stock. If each box has 300 apples and he sells 3/4 of his stock in a certain week, what total number of apples is not sold?"""
    
    # Determine the number of apples in each box
    apples_per_box = 300

    # Determine the number of boxes Kohen orders
    boxes_ordered = 10

    # Determine the total number of apples in Kohen's stock
    total_apples = boxes_ordered * apples_per_box

    # Determine the number of apples Kohen sells
    apples_sold = total_apples * 3/4

    # Determine the number of apples not sold
    apples_not_sold = total_apples - apples_sold

    # Display the total number of apples not sold
    result = apples_not_sold
    return result

print(solution())