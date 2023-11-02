def solution():
    """Nala found 5 seashells at the beach. The next day, she found another 7, and the following day, she found twice the number she got from the first two days. How many seashells does Nala have?"""
    
    # Define the number of seashells Nala found on the first day
    day1 = 5
    
    # Define the number of seashells Nala found on the second day
    day2 = 7
    
    # Define the number of seashells Nala found on the third day as twice the sum of the first two days
    day3 = (day1 + day2) * 2
    
    # Calculate the total number of seashells Nala has
    total_seashells = day1 + day2 + day3
    
    # Display the total number of seashells Nala has
    result = total_seashells
    return result

print(solution())