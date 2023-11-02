def solution():
    packaged_bread = 2
    packaged_ham = 2
    slices_of_bread = 20
    slices_of_ham = 8
    sandwiches = min(slices_of_bread, slices_of_ham)
    leftover_bread = slices_of_bread - sandwiches
    result = leftover_bread
    
    return result

print(solution())