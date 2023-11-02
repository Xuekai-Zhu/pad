def solution():
    Sunday_glasses = 2
    Monday_glasses = 4
    Tuesday_glasses = 3
    Wednesday_glasses = 3
    Thursday_glasses = 3
    Friday_glasses = 3
    Saturday_glasses = 3
    water_needed = 220
    total_water = Sunday_glasses + Monday_glasses + Tuesday_glasses + Wednesday_glasses + Thursday_glasses + Friday_glasses
    result = water_needed - total_water
    return result

print(solution())