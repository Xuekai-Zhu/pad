def solution():
    # Calculate the total revenue from ticket sales
    total_revenue = 500 * 30

    # Calculate the portion of revenue that goes to the band
    band_share = 0.7 * total_revenue 

    # Calculate the amount each band member gets
    member_share = band_share / 4
    result = member_share
    return result

print(solution())