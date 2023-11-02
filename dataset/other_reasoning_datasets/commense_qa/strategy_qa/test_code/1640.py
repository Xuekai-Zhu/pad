def solution():
    # Declare variables to represent the possible causes of damage from beaver dams
    causes = ["flooding", "soil loosening", "soil erosion"]
    # Check if any of the causes are present, indicating potential damage to the land
    if any(causes):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())