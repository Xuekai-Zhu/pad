def solution():
    """Lovely cuts her birthday cake into 12 equal pieces. Only one-fourth of the cake was eaten by her visitors and the rest were kept. How many slices of cake were kept?"""
    total_slices = 12
    eaten_slices = total_slices // 4
    kept_slices = total_slices - eaten_slices
    result = kept_slices
    return result

print(solution())