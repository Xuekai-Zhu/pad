def solution():
    # Define the necessary elements to create a thermonuclear bomb
    necessary_elements = ["hydrogen"]
    # Check if sulfenic acid in onions contains the necessary elements
    onion_chemicals = ["sulfenic acid", "hydrogen"]
    if all(elem in onion_chemicals for elem in necessary_elements):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())