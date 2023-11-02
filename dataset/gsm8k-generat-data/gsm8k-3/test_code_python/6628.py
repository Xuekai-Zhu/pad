def solution():
    """Tracy set up a booth at an art fair. 20 people came to look at her art. Four of those customers bought two paintings each. The next 12 of those customers bought one painting each. The last 4 customers bought four paintings each. How many paintings did Tracy sell at the art fair?"""
    # Calculate the number of paintings sold to customers who bought two paintings each
    paintings_2 = 4 * 2

    # Calculate the number of paintings sold to customers who bought one painting each
    paintings_1 = 12 * 1

    # Calculate the number of paintings sold to customers who bought four paintings each
    paintings_4 = 4 * 4

    # Calculate the total number of paintings sold
    total_paintings = paintings_2 + paintings_1 + paintings_4

    # Display the total number of paintings sold
    result = total_paintings
    return result

print(solution())