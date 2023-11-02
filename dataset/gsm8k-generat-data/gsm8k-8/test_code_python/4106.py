def solution():
    # Define variables for each boy's can collection
    solomon_cans = 66
    juwan_cans = solomon_cans / 3
    levi_cans = juwan_cans / 2

    # Calculate the total can collection
    total_cans = solomon_cans + juwan_cans + levi_cans
    result = total_cans
    return result

print(solution())