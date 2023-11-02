def solution():
    """Matt skips ropes 3 times per second.  If he jumped for 10 minutes how many skips hops did he get?"""
    
    # Convert 10 minutes to seconds
    time_in_sec = 10 * 60
    
    # Calculate the total number of skips hops
    total_skips_hops = 3 * time_in_sec
    
    # Display the total number of skips hops
    result = total_skips_hops
    return result

print(solution())