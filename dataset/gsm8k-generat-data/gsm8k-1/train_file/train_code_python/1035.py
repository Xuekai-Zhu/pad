def solution():
    """Alia has 2 times as many markers as Austin. Austin has one-third as many markers as Steve does. If Steve has 60 markers, how many does Alia have?"""
    steve_markers = 60
    austin_markers = steve_markers / 3
    alia_markers = austin_markers * 2
    result = alia_markers
    return result

print(solution())