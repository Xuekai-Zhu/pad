def solution():
    
    preprinted_delegates = 16
    remaining_delegates = 36 - preprinted_delegates
    handmade_delegates = remaining_delegates / 2
    unbadged_delegates = 36 - preprinted_delegates - handmade_delegates
    result = unbadged_delegates
    return result

print(solution())