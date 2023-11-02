def solution():
    # Calculate the number of pens and notebooks on the shelf
    num_notebooks = 30  # given
    num_pens = num_notebooks + 50  # given
    total_items = num_notebooks + num_pens  # total items on the shelf

    result = (num_notebooks, num_pens, total_items)
    return result

print(solution())