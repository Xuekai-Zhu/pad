def solution():
    # Calculate the total number of apples in 10 boxes
    apples_per_box = 300
    total_apples_ordered = apples_per_box * 10

    # Calculate the number of apples sold in a week
    percent_sold = 3/4
    total_apples_sold = percent_sold * total_apples_ordered

    # Calculate the number of unsold apples
    unsold_apples = total_apples_ordered - total_apples_sold
    result = unsold_apples
    return result

print(solution())