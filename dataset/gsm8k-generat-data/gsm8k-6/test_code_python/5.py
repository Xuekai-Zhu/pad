def solution():
    # Calculate the number of purple flowers
    purple_flowers = 10 * 1.8  # 80% more than the number of yellow flowers
    
    # Calculate the total number of yellow and purple flowers
    yellow_and_purple = 10 + purple_flowers
    
    # Calculate the number of green flowers
    green_flowers = yellow_and_purple * 0.25  # 25% as many as yellow and purple flowers
    
    # Calculate the total number of flowers in the garden
    total_flowers = yellow_and_purple + green_flowers
    
    result = total_flowers
    return result

print(solution())