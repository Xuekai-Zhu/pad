def solution():
    """Alyana has a pizza that is cut into 16 slices. After she and her friends finish eating, there are 4 slices left. If each of them ate 2 slices of pizza, how many people ate the pizza?"""
    remaining_slices = 4
    slices_per_person = 2
    slices_eaten = 16 - remaining_slices
    num_people = slices_eaten / slices_per_person
    result = num_people
    return result

print(solution())