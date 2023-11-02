def solution():
    # Let Chase's speed be x km/h. 
    # Then Cameron's speed is 2x km/h and Danielle's speed is 6x km/h.
    # Let the distance between Granville and Salisbury be d km.
    
    # Time taken by Danielle to travel from Granville to Salisbury is:
    time_Danielle = d / (6*x)
    
    # Converting time to minutes
    time_Chase = time_Danielle * 60
    
    result = time_Chase
    return result

print(solution())