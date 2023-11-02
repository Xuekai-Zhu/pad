def solution():
    # Calculate the number of paintings sold to customers who bought two
    paintings_sold_two = 4 * 2

    # Calculate the number of paintings sold to customers who bought one
    paintings_sold_one = 12 * 1

    # Calculate the number of paintings sold to customers who bought four
    paintings_sold_four = 4 * 4

    # Calculate the total number of paintings sold
    total_paintings_sold = paintings_sold_two + paintings_sold_one + paintings_sold_four
    result = total_paintings_sold
    return result

print(solution())