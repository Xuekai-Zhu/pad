def solution():
    """A zoo has 16 pandas, paired into mates (in the same zoo). Only 25% of the panda couples get pregnant after mating. If they each have one baby, how many panda babies are born?"""
    # Define the number of Panda pairs and the probability of each pair having a baby
    num_pairs = 16
    p_baby = 0.25

    # Calculate the number of baby Pandas
    num_babies = int(num_pairs * p_baby)

    # Display the number of baby Pandas
    result = num_babies
    return result

print(solution())