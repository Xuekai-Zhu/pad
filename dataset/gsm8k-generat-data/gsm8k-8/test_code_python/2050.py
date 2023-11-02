def solution():
    # Define the length of the first protest
    first_protest_length = 4

    # Calculate the length of the second protest, which is 25% longer than the first
    second_protest_length = first_protest_length + 0.25 * first_protest_length

    # Calculate the total length of time John spent protesting
    total_protest_length = first_protest_length + second_protest_length
    result = total_protest_length
    return result

print(solution())