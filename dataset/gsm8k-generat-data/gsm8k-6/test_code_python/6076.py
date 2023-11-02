def solution():
    # Add five new cows to the herd
    initial_herd = 51
    new_cows = 5
    total_herd = initial_herd + new_cows

    # Calculate the number of cows sold (a quarter of the herd)
    sold_cows = total_herd // 4

    # Calculate the number of cows left in the herd
    remaining_cows = total_herd - sold_cows

    result = remaining_cows
    return result

print(solution())