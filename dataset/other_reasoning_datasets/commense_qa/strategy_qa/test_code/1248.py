def solution():
    # Define the most common fur colors of mongooses and the Desert Camouflage color
    mongoose_fur_colors = ["brown", "gray"]
    desert_camouflage_colors = ["Café Au Lait brown", "Pastel Gray"]
    # Check if the common mongoose fur colors overlap with the Desert Camouflage colors
    overlap = [color for color in mongoose_fur_colors if color in desert_camouflage_colors]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())