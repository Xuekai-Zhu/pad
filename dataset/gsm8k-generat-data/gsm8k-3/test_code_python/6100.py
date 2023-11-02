def solution():
    """Grandma Olga has 3 daughters and 3 sons.  If all her daughters each have 6 sons, and each of her sons has 5 daughters, how many grandchildren does she have in total?"""
    # Define the number of daughters and sons
    num_daughters = 3
    num_sons = 3

    # Define the number of grandchildren per daughter and per son
    grand_per_daughter = 6
    grand_per_son = 5

    # Calculate the total number of grandchildren
    total_grand = (num_daughters * grand_per_daughter) + (num_sons * grand_per_son)

    # Display the total number of grandchildren
    result = total_grand
    return result

print(solution())