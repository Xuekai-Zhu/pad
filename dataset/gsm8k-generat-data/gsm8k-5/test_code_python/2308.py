def solution():
    bandages_used = 2 + 3  # Peggy used 2 bandages on her left knee and 3 on her right knee
    box_size = 24 - 8  # The box had 8 less than 2 dozen (24) bandages before Peggy used any
    bandages_left = box_size - bandages_used  # Calculate how many bandages are left in the box
    result = bandages_left
    return result

print(solution())