def solution():
    total_land = 80  # Abraham owns 80 square meters of unused land
    land1_sold = total_land / 2  # Abraham sold half of the land for $50
    land2_sold = total_land / 4  # Abraham sold 1/4 of his land for $30
    land3_sold = total_land - land1_sold - land2_sold  # Abraham sold the remaining land for $3 per square meter

    # Calculate the total earnings from selling all the land
    total_earnings = (land1_sold * 50) + (land2_sold * 30) + (land3_sold * 3)
    result = total_earnings
    return result

print(solution())