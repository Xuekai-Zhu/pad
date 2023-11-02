def solution():
    """Alyana has a pizza that is cut into 16 slices. After she and her friends finish eating, there are 4 slices left. If each of them ate 2 slices of pizza, how many people ate the pizza?"""
    # Calculate the number of slices eaten by Alyana and her friends
    slices_eaten = 16 - 4
    # Calculate the number of people who ate the pizza
    num_people = slices_eaten // 2

    # Display the number of people who ate the pizza
    result = num_people
    return result

print(solution())