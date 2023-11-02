def solution():
    """Anne is drawing pictures. She has 12 markers and she notices that each one lasts for about 1.5 drawings. If she has already made 8 drawings, how many more can she make before she runs out of markers?"""
    # Define the number of markers Anne has
    markers = 12

    # Define the number of drawings each marker can make
    drawings_per_marker = 1.5

    # Determine how many drawings Anne has already made
    drawings_made = 8

    # Calculate how many more drawings Anne can make
    drawings_left = int((markers * drawings_per_marker) - drawings_made)

    # Display the number of drawings Anne can still make
    result = drawings_left
    return result

print(solution())