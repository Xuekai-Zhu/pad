def solution():
    """Sally had 14 fries at lunch. Her friend Mark gave her one-third of his 36 fries at lunch. How many fries did Sally have for lunch after that?"""
    # Define the number of fries Sally had at the start of lunch
    sally_fries_start = 14
    
    # Define the number of fries Mark gave Sally
    mark_fries = 36/3
    
    # Calculate the total number of fries Sally had after Mark gave her some
    total_fries = sally_fries_start + mark_fries
    
    # Display the total number of fries Sally had
    result = total_fries
    return result

print(solution())