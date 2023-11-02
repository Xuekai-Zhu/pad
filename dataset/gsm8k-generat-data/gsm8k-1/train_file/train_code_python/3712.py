def solution():
    """Lovely cuts her birthday cake into 12 equal pieces. Only one-fourth of the cake was eaten by her visitors and the rest were kept. How many slices of cake were kept?"""
    total_slices = 12
    slices_eaten = total_slices // 4
    slices_kept = total_slices - slices_eaten
    result = slices_kept
    return result

print(solution())