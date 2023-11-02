def solution():
    # Calculate the number of artichokes Hakeem can buy
    num_artichokes = int(15 / 1.25)  # round down to the nearest whole number

    # Calculate the total amount of dip Hakeem can make
    total_dip = num_artichokes * (5/3)  # 3 artichokes make 5 ounces of dip

    result = total_dip
    return result

print(solution())