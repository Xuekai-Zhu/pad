def solution():
    """Missy watches 5 28-minute reality shows and one 10-minute cartoon. How long does she spend watching TV?"""
    # Define the length of each show in minutes
    REALITY_SHOW_LENGTH = 28
    CARTOON_LENGTH = 10

    # Calculate the total length of all the reality shows
    reality_show_total_length = REALITY_SHOW_LENGTH * 5

    # Calculate the total length of all the shows
    total_length = reality_show_total_length + CARTOON_LENGTH

    # Display the total length
    result = total_length
    return result

print(solution())