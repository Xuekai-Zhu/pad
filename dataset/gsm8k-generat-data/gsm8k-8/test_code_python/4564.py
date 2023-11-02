def solution():
    # Define the total number of hoodies and the difference in number of hoodies
    total_hoodies = 8
    difference = 2

    # Use algebra to find the number of hoodies each person owns
    fiona_hoodies = (total_hoodies - difference) / 2
    casey_hoodies = fiona_hoodies + difference

    # Return the number of hoodies Fiona owns
    result = fiona_hoodies
    return result

print(solution())