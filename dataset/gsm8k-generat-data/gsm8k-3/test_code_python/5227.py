def solution():
    """Julian has 400 legos and wants to make lego models of two identical airplanes. If each airplane model requires 240 legos, how many more legos does Julian need?"""
    # Define the number of legos Julian wants to use for each airplane model
    legos_per_airplane = 240

    # Calculate the total number of legos needed for both airplane models
    total_legos_needed = legos_per_airplane * 2

    # Calculate the number of legos Julian still needs
    additional_legos_needed = total_legos_needed - 400

    # Display the number of additional legos Julian needs
    result = additional_legos_needed
    return result

print(solution())