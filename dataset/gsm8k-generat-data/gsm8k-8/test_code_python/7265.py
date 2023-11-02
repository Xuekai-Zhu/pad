def solution():
    # Calculate Michael's share
    michael_share = 60 / 2

    # Calculate Paige's share
    paige_share = (60 - michael_share) / 2

    # Calculate Mandy's share
    mandy_share = 60 - michael_share - paige_share
    result = mandy_share
    return result

print(solution())