def solution():
    """Parker is 4 inches shorter than Daisy. Daisy is 8 inches taller than Reese. If Reese is 60 inches tall, what is the average height for the three of them?"""
    # Define the height of Reese
    reese_height = 60

    # Calculate the height of Daisy
    daisy_height = reese_height + 8

    # Calculate the height of Parker
    parker_height = daisy_height - 4

    # Calculate the average height of the three
    average_height = (reese_height + daisy_height + parker_height) / 3

    # Display the average height
    result = average_height
    return result

print(solution())