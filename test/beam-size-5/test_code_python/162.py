def solution():
    eggs_per_babysitting = 9  # Sandra's neighbor gives her a basket of 9 eggs every time she babysits their daughter
    eggs_per_flan = 3  # Sandra needs 3 eggs to make a Spanish flan
    flans_to_make = 15  # Sandra has been tasked to make 15 Spanish flans

    # Calculate the total number of eggs Sandra has to babysit
    total_eggs = eggs_per_flan * flans_to_make

    # Calculate the number of times Sandra needs to babysit
    babysit_count = total_eggs // eggs_per_babysitting
    result = babysit_count
    return result

print(solution())