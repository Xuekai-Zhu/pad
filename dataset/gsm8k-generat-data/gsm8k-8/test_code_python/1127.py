def solution():
    # Define the percentage of useful and junk items
    useful_percentage = 20
    junk_percentage = 70

    # Calculate the total number of items by assuming there are 100 items in total
    total_items = 100

    # Calculate the number of useful items in actual numbers
    useful_items = (useful_percentage/100) * total_items

    # Calculate the number of junk items in actual numbers
    junk_items = (junk_percentage/100) * total_items

    # Use the ratio of the number of useful items to calculate the number of junk items
    junk_items = junk_items / useful_items * 8

    result = junk_items
    return result

print(solution())