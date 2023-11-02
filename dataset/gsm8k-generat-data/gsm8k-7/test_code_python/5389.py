def solution():
    num_cats = 1
    claws_per_cat = 4

    time_per_nail = 10
    num_nails_per_cat = claws_per_cat * num_cats

    time_per_ear = 90

    time_for_shampoo = 5*60  # convert 5 minutes to seconds

    # Calculate the total time taken to groom one cat
    total_time_per_cat = (num_nails_per_cat * time_per_nail) + time_per_ear + time_for_shampoo

    result = total_time_per_cat
    return result

print(solution())