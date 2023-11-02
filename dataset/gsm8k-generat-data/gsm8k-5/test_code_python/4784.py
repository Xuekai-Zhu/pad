def solution():
    lions = 200  # Given that the number of lions in the park is 200
    leopards = lions / 2  # The total number of lions is twice the number of leopards
    elephants = (lions + leopards) / 2  # The number of elephants is half the combined number of lions and leopards
    total_population = lions + leopards + elephants  # Calculate the total population of the three animals in the park

    result = total_population
    return result

print(solution())