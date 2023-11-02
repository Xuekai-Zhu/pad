def solution():
    num_frogs = 5
    tadpole_to_frog_ratio = 3
    survival_rate = 2/3
    max_frogs = 8

    # Calculate the total number of tadpoles
    num_tadpoles = num_frogs * tadpole_to_frog_ratio

    # Calculate how many tadpoles will become mature frogs
    num_mature_frogs = num_tadpoles * survival_rate

    # Calculate how many frogs will have to find a new pond
    num_frogs_to_move = num_mature_frogs - max_frogs

    result = num_frogs_to_move
    return result

print(solution())