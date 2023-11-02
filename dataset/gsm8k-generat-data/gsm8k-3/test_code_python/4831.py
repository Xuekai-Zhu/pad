def solution():
    """Joyce moved to the countryside because she needed more farmland to grow her vegetables.  Her new property is 10 times larger than her previous property, but her new land has a 1-acre pond on it where she cannot grow vegetables.  If her previous property was 2 acres, how many acres of land does she now own that are suitable for growing vegetables?"""
    
    # Define the size of Joyce's previous property
    previous_size = 2
    
    # Define the size of the pond on Joyce's new property
    pond_size = 1
    
    # Calculate the size of Joyce's new property
    new_size = previous_size * 10
    
    # Calculate the size of the land suitable for growing vegetables on Joyce's new property
    veggie_size = new_size - pond_size
    
    # Display the size of the land suitable for growing vegetables on Joyce's new property
    result = veggie_size
    return result

print(solution())