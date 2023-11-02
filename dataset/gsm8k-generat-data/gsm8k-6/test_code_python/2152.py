def solution():
    # Calculate the number of jellybeans each nephew or niece received
    num_nephews_nieces = 3 + 2  # total number of nephews and nieces
    jellybeans_each = 70 // num_nephews_nieces  # divide the jellybeans equally
    result = jellybeans_each
    return result

print(solution())