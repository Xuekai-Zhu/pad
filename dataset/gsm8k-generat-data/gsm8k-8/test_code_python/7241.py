def solution():
    # Calculate the number of roses in Claire's garden
    total_roses = 400 - 120
    # Calculate the number of white roses
    white_roses = 80
    # Calculate the number of red roses
    red_roses = total_roses - white_roses
    # Calculate the total earnings if Claire sells all the red roses
    total_earnings = red_roses * 0.75
    # Calculate the earnings if Claire sells half of the red roses
    half_earnings = total_earnings / 2
    result = half_earnings
    return result

print(solution())