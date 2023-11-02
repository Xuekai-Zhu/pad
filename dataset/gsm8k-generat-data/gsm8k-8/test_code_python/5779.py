def solution():
    # Define the ratio of red beads to blue beads
    red_to_blue_ratio = 3/2
    
    # Calculate the number of blue beads with the given number of red beads
    num_red_beads = 30
    num_blue_beads = (num_red_beads * 2) / red_to_blue_ratio
    
    result = num_blue_beads
    return result

print(solution())