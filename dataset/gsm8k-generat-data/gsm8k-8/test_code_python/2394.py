def solution():
    # Define the number of raccoons and the number of squirrels as variables
    raccoons = x
    squirrels = 6 * x

    # Set up an equation using the total number of animals sprayed
    total_animals = raccoons + squirrels
    total_animals_sprayed = 84
    raccoons_sprayed = x

    # Solve for the number of raccoons sprayed
    raccoons_sprayed = total_animals_sprayed / (6 + 1)
    result = raccoons_sprayed
    return result

print(solution())