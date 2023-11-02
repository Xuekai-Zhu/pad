def solution():
    """Olga has three stripes on the side of each of her tennis shoes. Rick has one less stripe per shoe than does Olga. But Hortense has double the number of stripes on her tennis shoes as does Olga. In total, what is the combined number of stripes on all of their pairs of tennis shoes?"""
    # Define the number of stripes on Olga's shoes
    olga_stripes = 3

    # Calculate the number of stripes on Rick's shoes
    rick_stripes = olga_stripes - 1

    # Calculate the number of stripes on Hortense's shoes
    hortense_stripes = olga_stripes * 2

    # Calculate the total number of stripes on their shoes
    total_stripes = (olga_stripes + rick_stripes) * 2 + hortense_stripes * 2

    result = total_stripes
    return result

print(solution())