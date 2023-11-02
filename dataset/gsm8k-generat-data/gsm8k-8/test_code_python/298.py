def solution():
    # Define the number of sweets that Jack took
    jack_sweets = 4 + (1/2) * total_sweets

    # Calculate the total number of sweets
    total_sweets = 2 * (jack_sweets + 7)

    result = int(total_sweets)
    return result

print(solution())