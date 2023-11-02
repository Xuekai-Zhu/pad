def solution():
    # Set up the ratio of Parker's share to Richie's share
    parker_to_richie = 2/3
    
    # Determine how much Richie got
    richie_share = 50 / parker_to_richie * (3/2)
    
    # Calculate the total amount shared
    total_share = richie_share + 50
    
    result = total_share
    return result

print(solution())