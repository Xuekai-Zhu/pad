def solution():
    num_sausages = 3
    sausage_time = 5
    num_eggs = 6
    egg_time = 4

    # Calculate the total time for cooking sausages
    sausage_total_time = num_sausages * sausage_time

    # Calculate the total time for scrambling eggs
    egg_total_time = num_eggs * egg_time

    # Calculate the total time taken for making breakfast
    total_time = sausage_total_time + egg_total_time
    result = total_time
    return result

print(solution())