def solution():
    time_per_skirt = 2  # Alexis can sew a skirt in 2 hours
    time_per_coat = 7  # Alexis can sew a coat in 7 hours
    skirts_to_sew = 6  # Alexis needs to sew 6 skirts
    coats_to_sew = 4  # Alexis needs to sew 4 coats

    # Calculate the total time to sew all the skirts and coats
    total_time = (time_per_skirt * skirts_to_sew) + (time_per_coat * coats_to_sew)
    result = total_time
    return result

print(solution())