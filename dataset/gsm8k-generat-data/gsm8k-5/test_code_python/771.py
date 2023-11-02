def solution():
    sandwiches = 8  # Jimmy makes 8 sandwiches in total
    bread_slices_per_sandwich = 2  # Each sandwich requires 2 slices of bread
    bread_slices_needed = sandwiches * bread_slices_per_sandwich  # Calculate total bread slices needed
    bread_slices_per_pack = 4  # Each pack of bread has 4 slices
    packs_of_bread_needed = bread_slices_needed // bread_slices_per_pack + int(bread_slices_needed % bread_slices_per_pack != 0)
    # Calculate packs of bread needed, rounding up if needed
    result = packs_of_bread_needed
    return result

print(solution())