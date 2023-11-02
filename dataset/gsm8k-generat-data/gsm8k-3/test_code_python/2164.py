def solution():
    """There are 24 toys in the box and ¼ of them are action figures. The remaining toys are all dolls. How many dolls are there?"""
    # Calculate the number of action figures
    action_figures = 24 * 0.25

    # Calculate the number of dolls
    dolls = 24 - action_figures

    # Display the number of dolls
    result = dolls
    return result

print(solution())