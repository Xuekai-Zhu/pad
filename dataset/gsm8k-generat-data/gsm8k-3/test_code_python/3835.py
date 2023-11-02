def solution():
    """Billy is breeding mice for an experiment. He starts with 8 mice, who each have 6 pups. When the pups grow up, all the mice have another 6 pups. Then each adult mouse eats 2 of their pups due to the stress of overcrowding. How many mice are left?"""
    # Define the initial number of mice
    num_mice = 8

    # Calculate the number of pups in the first generation
    num_pups_1 = num_mice * 6

    # Calculate the number of mice in the second generation
    num_mice_2 = num_pups_1 * 6

    # Calculate the number of mice that are eaten
    num_eaten = num_mice_2 * 2

    # Calculate the final number of mice
    num_left = num_mice + num_pups_1 + num_mice_2 - num_eaten

    # Display the final number of mice
    result = num_left
    return result

print(solution())