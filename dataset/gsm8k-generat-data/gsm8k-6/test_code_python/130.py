def solution():
    # Calculate the number of seashells left after giving some to friends and brothers
    num_seashells = 180 - 40 - 30  
    # Calculate the number of seashells sold
    num_sold = num_seashells / 2  
    # Calculate the number of seashells left after selling half
    num_left = num_seashells - num_sold 

    result = num_left
    return result

print(solution())