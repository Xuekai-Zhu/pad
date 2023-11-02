def solution():
    """Parker is 4 inches shorter than Daisy. Daisy is 8 inches taller than Reese. If Reese is 60 inches tall, what is the average height for the three of them?"""
    reese_height = 60
    daisy_height = reese_height + 8
    parker_height = daisy_height - 4
    total_height = reese_height + daisy_height + parker_height
    average_height = total_height / 3
    result = average_height
    return result

print(solution())