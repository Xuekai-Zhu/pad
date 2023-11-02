def solution():
    # Calculate the total donation amount based on kilometers run
    first_km_donation = 10
    total_donation = first_km_donation
    for km in range(2, 6):
        donation = first_km_donation * (2 ** (km - 1))
        total_donation += donation
    result = total_donation
    return result

print(solution())