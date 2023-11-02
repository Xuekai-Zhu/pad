def solution():
    """A bar of steel weighs twice the mass of a bar of tin. If a steel bar also 
    weighs 20 kgs more than a copper bar and a copper bar weighs 90 kgs, 
    calculate the total weight of a container with 20 bars of each type of metal."""
    # Define the weight of a copper bar
    copper_weight = 90

    # Calculate the weight of a steel bar
    steel_weight = copper_weight + 20

    # Calculate the weight of a tin bar
    tin_weight = steel_weight / 2

    # Calculate the total weight of 20 bars of each type of metal
    total_weight = (copper_weight * 20) + (steel_weight * 20) + (tin_weight * 20)

    # Display the total weight
    result = total_weight
    return result

print(solution())