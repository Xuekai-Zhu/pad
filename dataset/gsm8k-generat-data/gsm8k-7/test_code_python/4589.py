def solution():
    num_eggs = 60
    egg_clean_time = 15
    num_toilet_paper_rolls = 7
    tp_clean_time = 30

    # Calculate the total cleaning time for the eggs
    egg_clean_total = num_eggs * egg_clean_time

    # Calculate the total cleaning time for the toilet paper
    tp_clean_total = num_toilet_paper_rolls * tp_clean_time

    # Calculate the total cleaning time in minutes
    total_clean_time = (egg_clean_total + tp_clean_total) / 60
    result = total_clean_time
    return result

print(solution())