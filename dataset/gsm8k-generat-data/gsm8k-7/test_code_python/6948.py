def solution():
    total_pits = 80
    sprout_percent = 0.25
    saplings_sold = 6

    # Calculate the number of sprouted pits
    sprouted_pits = total_pits * sprout_percent

    # Calculate the number of cherry saplings left after selling some
    num_saplings_left = sprouted_pits - saplings_sold
    result = num_saplings_left
    return result

print(solution())