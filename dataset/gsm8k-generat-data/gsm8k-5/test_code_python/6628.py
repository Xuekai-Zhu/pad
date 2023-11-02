def solution():
    # Calculate the number of paintings sold to customers who bought two
    paintings_two = 4 * 2

    # Calculate the number of paintings sold to customers who bought one
    paintings_one = 12 * 1

    # Calculate the number of paintings sold to customers who bought four
    paintings_four = 4 * 4

    # Calculate the total number of paintings sold
    total_paintings = paintings_two + paintings_one + paintings_four
    result = total_paintings
    return result

print(solution())