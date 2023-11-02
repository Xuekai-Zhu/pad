def solution():
    appetizers_per_guest = 6
    total_guests = 30
    appetizers_needed = appetizers_per_guest * total_guests
    appetizers_made = 3 + 2 + 2
    appetizers_left_to_make = appetizers_needed - appetizers_made
    dozens_left_to_make = appetizers_left_to_make / 12
    result = dozens_left_to_make
    return result

print(solution())