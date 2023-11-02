def solution():
    """Alyana has a pizza that is cut into 16 slices. After she and her friends finish eating, there are 4 slices left. If each of them ate 2 slices of pizza, how many people ate the pizza?"""
    # Define the total number of slices and the number of slices left
    total_slices = 16
    slices_left = 4

    # Calculate the number of slices eaten
    slices_eaten = total_slices - slices_left

    # Calculate the number of people who ate the pizza
    num_people = slices_eaten / 2

    # return the result
    result = num_people
    return result

print(solution())