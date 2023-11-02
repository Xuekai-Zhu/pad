def solution():
    """John attends a protest for 4 days. He then attends a second protest for 25% longer than the first. How many days did he spend protesting?"""
    # Define the length of the first protest in days
    first_protest_length = 4

    # Calculate the length of the second protest as 25% longer than the first
    second_protest_length = first_protest_length * 1.25

    # Calculate the total length of time spent protesting
    total_protest_length = first_protest_length + second_protest_length

    # Return the result
    result = total_protest_length
    return result

print(solution())