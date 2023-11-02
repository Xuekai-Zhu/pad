def solution():
    total_roses = 80  # Mrs. Amaro has 80 roses in her garden
    red_roses = (3 / 4) * total_roses  # Three-fourths of her roses are red
    remaining_roses = total_roses - red_roses  # Calculate the remaining roses
    yellow_roses = (1 / 4) * remaining_roses  # One-fourth of the remaining roses are yellow
    white_roses = remaining_roses - yellow_roses  # The rest are white

    # Calculate the number of roses that are either red or white
    red_or_white_roses = red_roses + white_roses
    result = red_or_white_roses
    return result

print(solution())