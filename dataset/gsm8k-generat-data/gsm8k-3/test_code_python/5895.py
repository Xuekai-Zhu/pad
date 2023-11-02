def solution():
    """Mark can jump 6 inches off the ground. Lisa can jump double the height as Mark, and Jacob can jump double the height of Lisa. If James jumps 2/3 as high Jacob, how high can James jump?"""
    
    # Define Mark's jump height
    mark_jump = 6
    
    # Define Lisa's jump height
    lisa_jump = mark_jump * 2
    
    # Define Jacob's jump height
    jacob_jump = lisa_jump * 2
    
    # Define James' jump height
    james_jump = jacob_jump * (2/3)
    
    # Display James' jump height
    result = james_jump
    return result

print(solution())