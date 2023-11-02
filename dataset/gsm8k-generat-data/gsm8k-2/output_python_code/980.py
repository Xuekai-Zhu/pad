def solution():
    """Olga has three stripes on the side of each of her tennis shoes. Rick has one less stripe per shoe than does Olga. But Hortense has double the number of stripes on her tennis shoes as does Olga. In total, what is the combined number of stripes on all of their pairs of tennis shoes?"""
    olga_stripes = 3
    rick_stripes = olga_stripes - 1
    hortense_stripes = olga_stripes * 2
    total_stripes = (olga_stripes * 2) + (rick_stripes * 2) + (hortense_stripes * 2)
    result = total_stripes
    return result

print(solution())