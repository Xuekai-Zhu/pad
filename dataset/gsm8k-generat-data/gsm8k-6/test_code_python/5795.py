def solution():
    # Calculate the number of roses, tulips, and carnations bought by Ariana
    roses = (2/5) * 40  # 2/5 of the flowers were roses
    tulips = 10  # Ariana bought 10 tulips
    carnations = 40 - roses - tulips  # the rest of the flowers were carnations
    result = carnations
    return result

print(solution())