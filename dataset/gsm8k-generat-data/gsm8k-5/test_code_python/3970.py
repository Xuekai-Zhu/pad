def solution():
    normal_batch = 1  # We'll assume a normal batch requires 1 can of each ingredient
    chili_cans = 4 * (normal_batch + 1)  # For a quadruple batch, Carla adds 1 can of chilis to each normal batch
    bean_cans = 4 * (2 * normal_batch)  # For a quadruple batch, Carla adds 2 cans of beans to each normal batch
    tomato_cans = 4 * (1.5 * 2 * normal_batch)  # For a quadruple batch, Carla adds 50% more tomatoes than beans to each normal batch

    # Calculate the total number of cans of food Carla needs
    total_cans = chili_cans + bean_cans + tomato_cans
    result = total_cans
    return result

print(solution())