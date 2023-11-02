def solution():
    reese_height = 60  # Reese is 60 inches tall
    daisy_height = reese_height + 8  # Daisy is 8 inches taller than Reese
    parker_height = daisy_height - 4  # Parker is 4 inches shorter than Daisy

    # Calculate the average height
    total_height = reese_height + daisy_height + parker_height
    average_height = total_height / 3
    result = average_height
    return result

print(solution())