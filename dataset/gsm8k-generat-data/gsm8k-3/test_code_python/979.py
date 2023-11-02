def solution():
    """At football tryouts, the coach wanted to see who could throw the ball the farthest.  Parker threw the ball 16 yards.  
    Grant threw the ball 25 percent farther than Parker and Kyle threw the ball 2 times farther than Grant. 
    Compared to Parker, how much farther did Kyle throw the ball?"""
    
    # Parker's throw
    parker_throw = 16
    
    # Grant's throw
    grant_throw = parker_throw * 1.25
    
    # Kyle's throw 
    kyle_throw = grant_throw * 2
    
    # Compared to Parker, how much farther did Kyle throw the ball?
    distance_further = kyle_throw - parker_throw
    
    # Display the distance further
    result = distance_further
    return result

print(solution())