def solution():
    """Mark has a garden with flowers. He planted plants of three different colors in it. Ten of them are yellow, and there are 80% more of those in purple.
    There are only 25% as many green flowers as there are yellow and purple flowers. How many flowers does Mark have in his garden?"""
    
    # Define the initial number of yellow flowers
    yellow_flowers = 10
    
    # Calculate the number of purple flowers
    purple_flowers = yellow_flowers * 0.8 + yellow_flowers
    
    # Calculate the total number of yellow and purple flowers
    yellow_and_purple_flowers = yellow_flowers + purple_flowers
    
    # Calculate the number of green flowers
    green_flowers = yellow_and_purple_flowers * 0.25
    
    # Calculate the total number of flowers
    total_flowers = yellow_and_purple_flowers + green_flowers
    
    # return the result
    result = total_flowers
    return result

print(solution())