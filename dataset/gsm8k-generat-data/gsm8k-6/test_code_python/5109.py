def solution():
    # Calculate the mask production in July
    mask_production_june = 2*2*3000  # mask production in June is double of March, doubled again in May
    mask_production_july = 2*mask_production_june  # mask production in July is double of June
    result = mask_production_july
    return result

print(solution())