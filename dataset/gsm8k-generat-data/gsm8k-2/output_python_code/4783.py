def solution():
    """The total number of lions in a park is twice the number of leopards in the same park. The number of elephants is half the combined number of lions and leopards. Calculate the total population of the three animals in the park if the number of lions is 200."""
    lions = 200
    leopards = lions / 2
    elephants = (lions + leopards) / 2
    total_population = lions + leopards + elephants
    result = total_population
    return result

print(solution())