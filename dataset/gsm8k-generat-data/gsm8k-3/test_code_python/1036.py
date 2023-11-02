def solution():
    """Alia has 2 times as many markers as Austin. Austin has one-third as many markers as Steve does. If Steve has 60 markers, how many does Alia have?"""
    # Define the number of markers Steve has
    steve_markers = 60

    # Determine how many markers Austin has (one-third as many as Steve)
    austin_markers = steve_markers / 3

    # Determine how many markers Alia has (2 times as many as Austin)
    alia_markers = 2 * austin_markers

    # Display the number of markers Alia has
    result = alia_markers
    return result

print(solution())