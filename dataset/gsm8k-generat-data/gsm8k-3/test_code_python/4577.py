def solution():
    """Augustus can make 3 milkshakes per hour while Luna can make 7 milkshakes per hour. If Augustus and Luna have been making milkshakes for 8 hours now, how many milkshakes have they made?"""
    # Define Augustus and Luna's milkshake rates per hour
    AUGUSTUS_RATE = 3
    LUNA_RATE = 7

    # Define the number of hours they have been making milkshakes
    hours = 8

    # Calculate the total number of milkshakes made by Augustus and Luna
    total_milkshakes = (AUGUSTUS_RATE + LUNA_RATE) * hours

    # Display the total number of milkshakes made
    result = total_milkshakes
    return result

print(solution())