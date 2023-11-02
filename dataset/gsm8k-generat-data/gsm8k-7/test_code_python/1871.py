def solution():
    num_notebooks = 30
    num_pens = num_notebooks + 50

    # Calculate the total number of items on the shelf
    total_items = num_notebooks + num_pens

    result = (num_notebooks, num_pens, total_items)
    return result

print(solution())