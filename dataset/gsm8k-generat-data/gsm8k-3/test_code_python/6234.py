def solution():
    """Three frogs are trying to hop across the road. The first frog takes 4 times as many hops as the second.  The second frog takes twice as many as the third.  If the three frogs took a total of 99 hops, how many hops did it take the second frog to cross the road?"""
    
    # Let the number of hops taken by third frog be x
    x = 1
    
    # Calculate number of hops taken by second frog
    y = 2*x
    
    # Calculate number of hops taken by first frog
    z = 4*y
    
    # Calculate total number of hops taken by all three frogs
    total_hops = x+y+z
    
    # Check if total number of hops is equal to 99
    while total_hops != 99:
        # If not equal, increment the value of x
        x += 1
        # Recalculate number of hops taken by second frog
        y = 2*x
        # Recalculate number of hops taken by first frog
        z = 4*y
        # Recalculate total number of hops
        total_hops = x+y+z
    
    # Display the number of hops taken by the second frog
    result = y
    return result

print(solution())