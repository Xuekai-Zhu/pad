def solution():
    # Calculate Tobias' total savings from allowance and lawn mowing
    savings = 5*3 + 15*4  # $5 allowance a month for 3 months plus $15 per lawn for 4 lawns

    # Calculate Tobias' earnings from shoveling driveways
    earnings = 95 + 15 - 15  # cost of shoes plus $15 in change minus earnings from mowing lawns

    # Calculate the number of driveways Tobias shoveled
    num_driveways = (earnings - savings) // 7  # each driveway earns $7, subtract savings and divide by 7

    result = num_driveways
    return result

print(solution())