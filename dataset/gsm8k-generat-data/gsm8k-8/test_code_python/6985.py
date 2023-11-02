def solution():
    # Define the hourly and per-item rates
    hourly_rate = 9
    restring_rate = 15
    grommet_rate = 10
    stencil_rate = 1

    # Calculate the earnings from hourly work
    hourly_earnings = hourly_rate * 8

    # Calculate the earnings from restringing racquets
    restring_earnings = restring_rate * 7

    # Calculate the earnings from changing grommets
    grommet_earnings = grommet_rate * 2

    # Calculate the earnings from painting stencils
    stencil_earnings = stencil_rate * 5

    # Calculate the total earnings
    total_earnings = hourly_earnings + restring_earnings + grommet_earnings + stencil_earnings
    result = total_earnings
    return result

print(solution())