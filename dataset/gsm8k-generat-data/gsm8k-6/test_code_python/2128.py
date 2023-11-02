def solution():
    # Calculate the total amount of water the students need in a day
    total_water_needed = 200 * 10  # 200 students, each drinking 10 cups of water

    # Calculate the number of jugs needed to hold the total amount of water
    jugs_needed = total_water_needed // 40  # each jug holds 40 cups of water

    # If the total amount of water needed is not evenly divisible by 40, one more jug is needed to hold the remaining water
    if total_water_needed % 40 != 0:
        jugs_needed += 1

    result = jugs_needed
    return result

print(solution())