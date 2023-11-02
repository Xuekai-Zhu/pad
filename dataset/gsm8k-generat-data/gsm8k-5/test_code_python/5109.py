def solution():
    mask_production_march = 3000  # The company produced 3000 masks in March
    doubling_factor = 2  # The mask production was doubled every month
    total_production_july = mask_production_march * doubling_factor ** 4  # July is 4 months away from March

    result = total_production_july
    return result

print(solution())