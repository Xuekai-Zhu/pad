def solution():
    man_share = 1/2
    sold_share = 1/10
    sold_share_price = 460

    # Calculate the remaining share after selling 1/10
    remaining_share = man_share - sold_share

    # Calculate the value of the remaining share
    remaining_share_price = sold_share_price / sold_share * remaining_share

    # Calculate the worth of the entire lot
    worth_of_lot = remaining_share_price / man_share * 2
    result = worth_of_lot
    return result

print(solution())