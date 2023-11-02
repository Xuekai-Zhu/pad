def solution():
    """Ryan wants to take 5 peanut butter sandwiches to the beach.  If each sandwich consists of 3 slices of bread how many slices does Ryan need to make 5 sandwiches?"""
    # Define the number of slices of bread per sandwich
    BREAD_PER_SANDWICH = 3

    # Define the number of sandwiches Ryan wants to make
    sandwiches = 5

    # Calculate the total number of bread slices needed
    total_slices = sandwiches * BREAD_PER_SANDWICH

    # Display the total number of bread slices needed
    result = total_slices
    return result

print(solution())