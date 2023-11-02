def solution():
    """Alia has 2 times as many markers as Austin. Austin has one-third as many markers as Steve does. If Steve has 60 markers, how many does Alia have?"""
    # Define the number of markers Steve has
    steve_markers = 60

    # Calculate the number of markers Austin has
    austin_markers = steve_markers / 3

    # Calculate the number of markers Alia has
    alia_markers = austin_markers * 2

    # return the result
    result = alia_markers
    return result

print(solution())