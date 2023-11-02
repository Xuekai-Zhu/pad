def solution():
    # Calculate the total number of bags of popcorn Shelby had
    total_popcorn = 12 + 10  # a dozen bags of buttered popcorn and 10 bags of caramel popcorn
    # Calculate the number of bags of popcorn Alan took for his friends
    alan_popcorn = 3 + 1  # 3 bags of buttered and 1 bag of caramel
    # Calculate the number of bags of popcorn Shelby has left for the party
    remaining_popcorn = total_popcorn - alan_popcorn
    result = remaining_popcorn
    return result

print(solution())