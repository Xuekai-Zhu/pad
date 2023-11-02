def solution():
    num_pens = 3
    pen_price = 1

    num_notebooks = 4
    notebook_price = 3

    num_folders = 2
    folder_price = 5

    total_cost = (num_pens * pen_price) + (num_notebooks * notebook_price) + (num_folders * folder_price)
    payment = 50
    change = payment - total_cost
    result = change
    return result

print(solution())