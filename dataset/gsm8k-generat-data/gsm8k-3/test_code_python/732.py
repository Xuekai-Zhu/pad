def solution():
    """If a tarantula has eight legs, and one tarantula egg sac can contain 1000 tarantulas, how many baby tarantula legs would be in one less than 5 egg sacs?"""
    # Define the number of egg sacs
    num_sacs = 4

    # Calculate the total number of baby tarantulas
    num_tarantulas = num_sacs * 1000

    # Calculate the total number of baby tarantula legs
    num_legs = num_tarantulas * 8

    # Display the total number of baby tarantula legs
    result = num_legs
    return result

print(solution())