def solution():
    """There are 24 toys in the box and ¼ of them are action figures. The remaining toys are all dolls. How many dolls are there?"""
    # Define the total number of toys
    total_toys = 24

    # Calculate the number of action figures
    action_figures = total_toys // 4

    # Calculate the number of dolls
    dolls = total_toys - action_figures

    result = dolls
    return result

print(solution())