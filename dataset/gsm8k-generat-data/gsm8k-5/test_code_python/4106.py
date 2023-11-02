def solution():
    solomon_cans = 66  # Solomon collected 66 cans
    juwan_cans = solomon_cans / 3  # Juwan collected a third of what Solomon collected
    levi_cans = juwan_cans / 2  # Levi collected half of what Juwan collected

    # Calculate the total number of cans collected by the boys
    total_cans = solomon_cans + juwan_cans + levi_cans
    result = total_cans
    return result

print(solution())