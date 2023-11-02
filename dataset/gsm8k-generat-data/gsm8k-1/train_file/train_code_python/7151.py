def solution():
    """Blanche, Rose and Dorothy liked to collect sea glass when they went to the beach. Blanche found 12 pieces of green and 3 pieces of red sea glass. Rose found 9 pieces of red and 11 pieces of blue sea glass. If Dorothy found twice as many pieces of red glass as Blanche and Rose and three times as much blue sea glass as Rose, how many pieces did Dorothy have?"""
    blanche_green = 12
    blanche_red = 3
    rose_red = 9
    rose_blue = 11
    dorothy_red = (blanche_red + rose_red) * 2
    dorothy_blue = rose_blue * 3
    dorothy_total = dorothy_red + dorothy_blue
    result = dorothy_total
    return result

print(solution())