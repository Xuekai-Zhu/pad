def solution():
    """Mara added 3 slices of cake to a plate that already had 2 slices on it. She was getting hungrier so she tripled the number of slices she currently has. She ate 2 slices and while she was distracted, her friend stole 5 slices off her plate. What number of cake slices remained on the plate?"""
    starting_slices = 2
    added_slices = 3
    total_slices = starting_slices + added_slices
    total_slices *= 3
    total_slices -= 2
    total_slices -= 5
    result = total_slices
    return result

print(solution())