def solution():
    engagement_ring = 4000  # John gave his fiancee a $4000 ring on their engagement day
    wedding_car = 2000  # John gave his fiancee a $2000 car as a gift on their wedding day
    diamond_bracelet = 2 * engagement_ring  # John gave his fiancee a diamond bracelet twice as expensive as the ring he gave her during the engagement

    # Calculate the total worth of the presents John gave to his fiancee
    total_presents = engagement_ring + wedding_car + diamond_bracelet
    result = total_presents
    return result

print(solution())