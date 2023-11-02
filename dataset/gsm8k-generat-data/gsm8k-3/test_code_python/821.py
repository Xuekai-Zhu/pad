def solution():
    """Sammy can eat 15 pickle slices.  His twin sister Tammy can eat twice as much as Sammy.  Their older brother Ron eats 20% fewer pickles slices than Tammy.  How many pickle slices does Ron eat?"""
    
    # Define the number of pickle slices that Sammy can eat
    sammy_slices = 15
    
    # Define the number of pickle slices that Tammy can eat
    tammy_slices = sammy_slices * 2
    
    # Calculate the number of pickle slices that Ron can eat
    ron_slices = tammy_slices * 0.8
    
    # Display the number of pickle slices that Ron can eat
    result = ron_slices
    return result

print(solution())