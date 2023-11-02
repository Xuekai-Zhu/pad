def solution():
    # Define the number of gemstones on Spaatz's collar
    spaatz_gemstones = 1

    # Calculate the number of gemstones on Frankie's collar
    frankie_gemstones = (spaatz_gemstones + 2) * 2

    # Calculate the number of gemstones on Binkie's collar
    binkie_gemstones = frankie_gemstones * 4

    result = binkie_gemstones
    return result

print(solution())