def solution():
    """Tony made a sandwich with two slices of bread for lunch every day this week. On Saturday, he was extra hungry from doing yard work and made two sandwiches. How many slices of bread are left from the 22-slice loaf Tony started with?"""
    # Define the number of slices of bread Tony started with
    starting_slices = 22

    # Calculate the number of slices of bread Tony used for lunch from Monday to Friday
    weekday_slices = 2 * 5

    # Calculate the number of slices of bread Tony used on Saturday
    saturday_slices = 2

    # Calculate the number of slices of bread Tony has left
    slices_left = starting_slices - weekday_slices - saturday_slices

    # return the result
    result = slices_left
    return result

print(solution())