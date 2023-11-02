def solution():
    num_friends = 3
    roger_cans = 4
    roger_brothers_cans = 2
    
    # Calculate the total number of cans after Roger gave some away
    total_cans = (num_friends + 1) * roger_cans + roger_brothers_cans
    
    # Calculate the number of cans Michelle had to start with
    michelle_cans = total_cans - roger_cans
    
    result = michelle_cans
    return result

print(solution())