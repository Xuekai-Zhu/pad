def solution():
    """Parker wants to find out what the average percentage of kernels that pop in a bag is. In the first bag he makes, 60 kernels pop and the bag has 75 kernels. In the second bag, 42 kernels pop and there are 50 in the bag. In the final bag, 82 kernels pop and the bag has 100 kernels."""
    # Define the number of popped kernels and total kernels in each bag
    bag1_popped = 60
    bag1_total = 75
    
    bag2_popped = 42
    bag2_total = 50
    
    bag3_popped = 82
    bag3_total = 100
    
    # Calculate the percentage of popped kernels in each bag
    bag1_percentage = (bag1_popped / bag1_total) * 100
    bag2_percentage = (bag2_popped / bag2_total) * 100
    bag3_percentage = (bag3_popped / bag3_total) * 100
    
    # Calculate the average percentage of popped kernels
    average_percentage = (bag1_percentage + bag2_percentage + bag3_percentage) / 3
    
    # Round the result to 2 decimal places
    result = round(average_percentage, 2)
    return result

print(solution())