def solution():
    # Define the percentage of married and single guests
    married_percent = 0.3
    single_percent = 0.5

    # Calculate the number of married and single guests
    married_count = married_percent * 1000
    single_count = single_percent * 1000

    # Calculate the number of children
    children_count = 1000 - married_count - single_count

    # Calculate the difference between the number of married people and children
    diff = married_count - children_count
    result = diff
    return result

print(solution())