def solution():
    # Hershel has 10 betta fish and 15 goldfish
    num_betta = 10
    num_goldfish = 15

    # Bexley brings 2/5 times as many betta fish and 1/3 times as many goldfish
    bexley_betta = 2/5 * num_betta
    bexley_goldfish = 1/3 * num_goldfish

    # Hershel now has the original fish plus the ones Bexley brought
    total_betta = num_betta + bexley_betta
    total_goldfish = num_goldfish + bexley_goldfish

    # Hershel gifts his sister 1/2 of the fish
    gift_betta = total_betta / 2
    gift_goldfish = total_goldfish / 2

    # Calculate the total number of fish Hershel has remaining
    remaining_fish = total_betta + total_goldfish - (gift_betta + gift_goldfish)
    result = remaining_fish
    return result

print(solution())