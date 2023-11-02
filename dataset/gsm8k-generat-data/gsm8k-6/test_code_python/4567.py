def solution():
    # Calculate the total number of books sold and received
    total_sold = 37 + 128 + 2*(37) + 128 + 34  # sold 37 books in-store on Saturday, sold 128 books online, sold twice as many in-store on Sunday, increased online sales by 34, received 160 new books
    current_inventory = 743 - total_sold  # calculate the current inventory by subtracting total books sold from the initial inventory of 743
    result = current_inventory
    return result

print(solution())