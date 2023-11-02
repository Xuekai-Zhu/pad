def solution():
    brown_stripes = 4  # There are 4 brown stripes
    gold_stripes = 3 * brown_stripes  # There are three times as many gold stripes as brown stripes
    blue_stripes = 5 * gold_stripes  # There are five times as many blue stripes as gold stripes

    total_stripes = brown_stripes + gold_stripes + blue_stripes  # Total number of stripes

    # Calculate the number of blue stripes
    blue_stripes_vaishalis = (blue_stripes / total_stripes) * 100
    result = blue_stripes_vaishalis
    return result

print(solution())