def solution():
    """Silvio was running a race that had 4 parts. The total length of the race was 74.5 kilometers. The first part of the race is 15.5 kilometers long. The second and third parts are each 21.5 kilometers long. How many kilometers is the last part of the race?"""
    # Define the total length of the race and the length of the first 3 parts
    total_length = 74.5
    first_length = 15.5
    second_length = 21.5
    third_length = 21.5

    # Calculate the length of the last part of the race
    last_length = total_length - first_length - second_length - third_length

    # Return the result
    result = last_length
    return result

print(solution())