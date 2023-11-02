def solution():
    flour_needed_per_cake = 100
    total_cakes = 9 + 9  # Traci and Harris made 9 cakes each

    # Calculate the total amount of flour needed for all cakes
    total_flour_needed = flour_needed_per_cake * total_cakes

    # Calculate the amount of flour Harris contributed
    harris_flour = 400

    # Calculate the amount of flour Traci brought from her own house
    traci_flour = total_flour_needed - harris_flour

    result = traci_flour
    return result

print(solution())