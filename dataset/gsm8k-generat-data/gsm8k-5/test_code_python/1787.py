def solution():
    sausages = 3
    eggs = 6
    time_per_sausage = 5
    time_per_egg = 4

    # Calculate the total time it took to fry the sausages
    total_sausage_time = sausages * time_per_sausage

    # Calculate the total time it took to scramble the eggs
    total_egg_time = eggs * time_per_egg

    # Calculate the total time it took to make breakfast
    total_time = total_sausage_time + total_egg_time
    result = total_time
    return result

print(solution())