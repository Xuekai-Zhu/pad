def solution():
    """James gets bored with his game so decides to play a different one. That game promises 100 hours of gameplay but 80% of that is boring grinding. However, the expansion does add another 30 hours of enjoyable gameplay. How much enjoyable gameplay does James get?"""
    # Define the total gameplay hours and the percentage of boring grinding
    total_hours = 100
    boring_percentage = 0.8

    # Calculate the total boring grinding hours and the enjoyable gameplay hours
    boring_hours = total_hours * boring_percentage
    enjoyable_hours = total_hours - boring_hours + 30

    # Return the result
    result = enjoyable_hours
    return result

print(solution())