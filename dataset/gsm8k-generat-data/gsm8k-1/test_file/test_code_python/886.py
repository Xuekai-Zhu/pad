def solution():
    """There are 100 plants in Mrs. Smith's garden. One-fourth of her plants are indoor plants. Two-thirds of the remaining are outdoor plants while the rest are flowering plants. What percent of the plants are flowering plants?"""
    total_plants = 100
    indoor_plants = total_plants // 4
    remaining_plants = total_plants - indoor_plants
    outdoor_plants = remaining_plants * 2 // 3
    flowering_plants = remaining_plants - outdoor_plants
    percent_flowering = (flowering_plants / total_plants) * 100
    result = percent_flowering
    return result

print(solution())