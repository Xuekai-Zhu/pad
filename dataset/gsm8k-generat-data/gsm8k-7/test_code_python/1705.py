def solution():
    num_dozen = 3
    num_free = 2
    num_flowers_per_dozen = 12

    # Calculate the total number of flowers that Maria will get
    total_flowers = (num_dozen + (num_dozen * num_free)) * num_flowers_per_dozen

    result = total_flowers
    return result

print(solution())