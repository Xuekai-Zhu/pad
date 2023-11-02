def solution():
    yellow_plants = 10  # Mark planted 10 yellow plants
    purple_plants = yellow_plants * 1.8  # There are 80% more purple plants than yellow plants
    total_yellow_purple_plants = yellow_plants + purple_plants  # Total number of yellow and purple plants
    green_plants = total_yellow_purple_plants * 0.25  # There are only 25% as many green plants as yellow and purple plants

    # Calculate the total number of plants in Mark's garden
    total_plants = yellow_plants + purple_plants + green_plants
    result = total_plants
    return result

print(solution())