def solution():
    # Set Hank Aaron's home run total
    hank_aaron_total = 755
    
    # Calculate twice Dave Winfield's home run total
    twice_winfield = 2 * ((hank_aaron_total) + 175)
    
    # Calculate Dave Winfield's home run total
    winfield_total = twice_winfield / 2
    
    result = winfield_total
    return result

print(solution())