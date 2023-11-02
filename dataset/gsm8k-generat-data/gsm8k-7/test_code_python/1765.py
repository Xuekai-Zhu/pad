def solution():
    num_babies = 6
    num_worms_per_baby_per_day = 3
    num_days = 3

    papa_bird_worms = 9
    mama_bird_worms = 13
    stolen_worms = 2

    # Calculate the total number of worms needed for all babies for 3 days
    total_worms_needed = num_babies * num_worms_per_baby_per_day * num_days

    # Calculate the total number of worms mama bird has
    total_worms_available = papa_bird_worms + mama_bird_worms - stolen_worms

    # Calculate the number of additional worms mama bird needs to catch
    additional_worms_needed = total_worms_needed - total_worms_available
    result = additional_worms_needed
    return result

print(solution())