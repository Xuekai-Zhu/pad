def solution():
    needed_flour = 6
    measuring_cup = 1/4
    total_flour_bag = 8

    # Calculate how many cups of flour Michael does not need
    unused_flour = total_flour_bag - needed_flour

    # Calculate how many measuring cups he needs to remove the unused flour
    num_scoops = unused_flour / measuring_cup
    result = num_scoops
    return result

print(solution())