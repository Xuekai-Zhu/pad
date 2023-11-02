def solution():
    """James gets bored with his game so decides to play a different one. That game promises 100 hours of gameplay but 80% of that is boring grinding. However, the expansion does add another 30 hours of enjoyable gameplay. How much enjoyable gameplay does James get?"""
    # Define the total hours of gameplay available and the percentage of boring grinding
    total_hours = 100
    boring_percentage = 80

    # Calculate the hours of enjoyable gameplay
    enjoyable_hours = total_hours * (100 - boring_percentage) / 100

    # Add the hours of enjoyable gameplay from the expansion
    enjoyable_hours += 30

    # Display the total hours of enjoyable gameplay
    result = enjoyable_hours
    return result

print(solution())