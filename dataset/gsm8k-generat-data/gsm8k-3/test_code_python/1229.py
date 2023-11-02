def solution():
    """Itzayana is 4 inches taller than Zora, who is 8 inches shorter than Brixton. If Zara is 64 inches tall and has the same height as Brixton, calculate the average height of the four people."""
    # Calculate the height of Brixton
    brixton_height = 64

    # Calculate the height of Zora
    zora_height = brixton_height - 8

    # Calculate the height of Itzayana
    itzayana_height = zora_height + 4

    # Calculate the total height of the four people
    total_height = brixton_height + zora_height + itzayana_height + 64

    # Calculate the average height
    average_height = total_height / 4

    # Display the average height
    result = average_height
    return result

print(solution())