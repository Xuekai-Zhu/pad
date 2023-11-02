def solution():
    # Define the size of the biggest doll and the size ratio
    biggest_doll_size = 243
    size_ratio = 2/3

    # Use a loop to find the size of the 6th smallest doll
    current_size = biggest_doll_size
    for i in range(5):
        current_size *= size_ratio
    
    result = round(current_size, 2)
    return result

print(solution())