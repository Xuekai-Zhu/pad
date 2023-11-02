def solution():
    """Lucy works in a pet shop. She can clean 2 aquariums in 3 hours. If Lucy is working 24 hours this week, how many aquariums could she clean?"""
    
    # Define the rate at which Lucy can clean aquariums (in terms of aquariums per hour)
    rate = 2/3
    
    # Define the number of hours Lucy is working this week
    hours_worked = 24
    
    # Calculate the number of aquariums Lucy can clean this week
    aquariums_cleaned = rate * hours_worked
    
    # Display the number of aquariums Lucy can clean
    result = aquariums_cleaned
    return result

print(solution())