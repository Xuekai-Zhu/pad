def solution():
    """Mark has 12 candy bars in total between Mars bars, Snickers, and Butterfingers. He has 3 Snickers and 2 Mars bars. How many Butterfingers does he have?"""
    
    # Define the number of Snickers and Mars bars
    snickers = 3
    mars = 2
    
    # Calculate the number of Butterfingers
    butterfingers = 12 - snickers - mars
    
    # return the result
    result = butterfingers
    return result

print(solution())