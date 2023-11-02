def solution():
    dancers = 8  # Jill has to braid 8 dancers' hair
    braids_per_dancer = 5  # Each dancer has 5 braids
    braid_time = 30  # Each braid takes 30 seconds

    # Calculate the total time needed to braid all dancers' hair
    total_braid_time = dancers * braids_per_dancer * braid_time

    # Convert the total braid time to minutes
    total_minutes = total_braid_time / 60
    result = total_minutes
    return result

print(solution())