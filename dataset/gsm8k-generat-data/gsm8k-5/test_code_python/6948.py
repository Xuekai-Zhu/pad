def solution():
    cherry_pits = 80  # Kim plants 80 cherry pits
    sprout_percentage = 0.25  # 25% of the cherry pits sprout
    sprouted_pits = cherry_pits * sprout_percentage  # Calculate the number of sprouted cherry pits
    saplings_sold = 6  # Kim sells 6 of the saplings
    remaining_saplings = sprouted_pits - saplings_sold  # Calculate the number of saplings Kim has left
    result = remaining_saplings
    return result

print(solution())