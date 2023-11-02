def solution():
    # Define the total number of words Keenan needs to write
    total_words = 1200

    # Define Keenan's writing speed in words per hour for the first 2 hours
    speed1 = 400

    # Calculate the number of words Keenan writes in the first 2 hours
    words1 = speed1 * 2

    # Define Keenan's writing speed in words per hour after the first 2 hours
    speed2 = 200

    # Calculate the remaining number of words Keenan needs to write
    remaining_words = total_words - words1

    # Calculate the number of hours Keenan needs to write the remaining words
    hours = remaining_words / speed2

    # Round up the number of hours to ensure Keenan finishes before the midnight deadline
    hours = math.ceil(hours)

    result = hours
    return result

print(solution())