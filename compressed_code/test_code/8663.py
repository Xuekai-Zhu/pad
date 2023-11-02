def solution():
    
    small_pizza = 4
    large_pizza = 8
    george_slices = 3
    bob_slices = george_slices + 1
    susie_slices = bob_slices / 2
    bill_slices = 3
    fred_slices = 3
    mark_slices = 3
    total_slices = (3 * small_pizza) + (2 * large_pizza)
    total_slices -= (george_slices + bob_slices + susie_slices 
                     + bill_slices + fred_slices + mark_slices)
    result = total_slices
    return result

print(solution())