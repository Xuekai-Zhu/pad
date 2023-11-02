def solution():
    """Chad is measuring the size of different countries. He sees that Canada is 1.5 times bigger than the United States and Russia is 1/3 bigger than Canada. How many times bigger is Russia than the United States?"""
    # Define the size of the United States
    US_size = 1

    # Calculate the size of Canada
    Canada_size = US_size * 1.5

    # Calculate the size of Russia
    Russia_size = Canada_size * 1.333

    # Calculate how many times bigger Russia is than the United States
    times_bigger = Russia_size / US_size

    # Display the result
    result = times_bigger
    return result

print(solution())