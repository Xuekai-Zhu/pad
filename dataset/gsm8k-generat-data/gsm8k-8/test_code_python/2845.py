def solution():
    # Calculate the total number of drops in 3 liters of blood
    total_drops = 5000 * 3

    # Calculate how many times a mosquito would need to feed to reach the total number of drops
    feed_times = total_drops / 20

    # Round up to the nearest whole number of feedings
    num_mosquitoes = math.ceil(feed_times)

    result = num_mosquitoes
    return result

print(solution())