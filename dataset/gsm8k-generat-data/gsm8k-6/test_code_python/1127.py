def solution():
    useful_items = 8  # number of useful items in the attic
    useful_percentage = 20  # percentage of items that are useful
    junk_percentage = 70  # percentage of items that are junk
    
    # Calculate the total number of items in the attic
    total_items = useful_items / (useful_percentage / 100)
    
    # Calculate the number of junk items in the attic
    junk_items = total_items - useful_items - (total_items * (10 / 100))
    result = junk_items
    return result

print(solution())