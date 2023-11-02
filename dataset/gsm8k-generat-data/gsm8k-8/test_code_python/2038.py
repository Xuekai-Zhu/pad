def solution():
    # Define the time it takes to cut each type of hair
    woman_time = 50
    man_time = 15
    kid_time = 25

    # Define the number of each type of hair Joe cut
    num_women = 3
    num_men = 2
    num_kids = 3

    # Calculate the total time Joe spent cutting hair
    total_time = (num_women * woman_time) + (num_men * man_time) + (num_kids * kid_time)
    result = total_time
    return result

print(solution())