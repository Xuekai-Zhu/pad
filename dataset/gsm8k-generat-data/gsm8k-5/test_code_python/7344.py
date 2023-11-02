def solution():
    total_cheerleaders = 19  # There are 19 cheerleaders in total
    num_size_2 = 4  # There are 4 cheerleaders who need size 2 uniforms
    num_size_12 = int(num_size_6 / 2)  # Half the number of size 6 cheerleaders need size 12 uniforms

    # Calculate the number of cheerleaders who need size 6 uniforms
    num_size_6 = total_cheerleaders - num_size_2 - num_size_12
    result = num_size_6
    return result

print(solution())