def solution():
    classmates = 30  # Justin needs to collect one flower for each classmate
    time_per_flower = 10  # It takes Justin on average 10 minutes to find a flower
    total_time = 120  # Justin has been gathering for 2 hours (120 minutes)
    flowers_initial = classmates  # Justin initially gathers one flower for each classmate
    flowers_lost = 3  # Justin has lost 3 of the flowers he initially gathered
    flowers_remaining = classmates - flowers_lost  # Justin needs to find flowers for his remaining classmates

    # Calculate the total time Justin needs to find flowers for his remaining classmates
    time_remaining = flowers_remaining * time_per_flower

    # Calculate the additional time Justin needs to look
    additional_time = time_remaining - (total_time - (flowers_initial * time_per_flower))

    result = additional_time
    return result

print(solution())