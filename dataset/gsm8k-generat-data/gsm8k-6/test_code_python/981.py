def solution():
    # Calculate the total number of stripes on all pairs of tennis shoes
    Olga_stripes = 3  # stripes on Olga's tennis shoes
    Rick_stripes = Olga_stripes - 1  # stripes on Rick's tennis shoes
    Hortense_stripes = 2 * Olga_stripes  # stripes on Hortense's tennis shoes
    total_stripes = 2 * (Olga_stripes + Rick_stripes + Hortense_stripes)  # total stripes on all pairs of tennis shoes
    result = total_stripes
    return result

print(solution())