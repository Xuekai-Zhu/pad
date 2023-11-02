def solution():
    """John went on a mission that was supposed to take 5 days.  Instead it took 60% longer.  He then had to go on a second mission which took 3 days.  How long was he on missions?"""
    # Define the original mission length and the percentage increase
    original_length = 5
    percentage_increase = 60

    # Calculate the new length of the mission
    new_length = original_length * (1 + percentage_increase/100)

    # Calculate the total length of both missions
    total_length = new_length + 3

    # Display the total length of both missions
    result = total_length
    return result

print(solution())