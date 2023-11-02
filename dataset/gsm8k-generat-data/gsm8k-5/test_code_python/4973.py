def solution():
    trout = 200  # James catches 200 pounds of trout
    salmon = (50/100)*trout + trout  # James catches 50% more pounds of salmon than trout
    tuna = 2*trout  # James catches twice as much tuna as trout

    # Calculate the total pounds of fish James caught
    total_fish = trout + salmon + tuna
    result = total_fish
    return result

print(solution())