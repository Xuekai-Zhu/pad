def solution():
    # Define the vitamins that basil contains
    basil_vitamins = ["A", "B", "C", "E", "K"]
    # Check if basil contains vitamin D
    if "D" in basil_vitamins:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())