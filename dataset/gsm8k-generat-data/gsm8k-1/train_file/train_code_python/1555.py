def solution():
    """Alyana has a pizza that is cut into 16 slices. After she and her friends finish eating, there are 4 slices left. If each of them ate 2 slices of pizza, how many people ate the pizza?"""
    total_slices = 16
    leftover_slices = 4
    eaten_slices = total_slices - leftover_slices
    slices_per_person = 2
    num_people = eaten_slices / slices_per_person
    result = num_people
    return result

print(solution())