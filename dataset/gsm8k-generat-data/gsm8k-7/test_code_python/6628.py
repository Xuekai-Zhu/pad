def solution():
    total_customers = 20

    # Calculate the number of paintings sold to customers who bought two paintings each
    num_paintings_2 = 4 * 2

    # Calculate the number of paintings sold to customers who bought one painting each
    num_paintings_1 = 12 * 1

    # Calculate the number of paintings sold to customers who bought four paintings each
    num_paintings_4 = 4 * 4

    # Calculate the total number of paintings sold
    total_paintings_sold = num_paintings_2 + num_paintings_1 + num_paintings_4
    result = total_paintings_sold
    return result

print(solution())