def solution():
    total_marbles = 400  # Leo had 400 marbles in a jar
    marbles_per_pack = 10  # Leo packed the marbles with 10 marbles in each pack

    # Calculate the total number of packs of marbles
    total_packs = total_marbles / marbles_per_pack

    # Calculate the number of packs Manny received
    manny_packs = total_packs / 4

    # Calculate the number of packs Neil received
    neil_packs = total_packs / 8

    # Calculate the number of packs Leo kept
    leo_packs = total_packs - manny_packs - neil_packs
    result = leo_packs
    return result

print(solution())