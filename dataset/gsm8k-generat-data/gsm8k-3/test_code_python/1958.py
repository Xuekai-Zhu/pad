def solution():
    """Prejean's speed in a race was three-quarters that of Rickey. If they both took a total of 70 minutes to run the race, calculate the total number of minutes that Rickey took to finish the race."""
    
    # Let's assume that Rickey's time for the race is x and his speed is v
    # Prejean's speed is 3/4 of Rickey's speed, so his speed is (3/4)*v
    
    # Using the formula distance = speed * time, we can write:
    
    # distance for Rickey = v * x
    # distance for Prejean = (3/4)*v * (70 - x)  (since they both took a total of 70 minutes)
    
    # The total distance is the same for both, so we can equate the two expressions above:
    
    # v * x = (3/4)*v * (70 - x)
    
    # Solving for x, we get:
    
    # x = 42
    
    # So Rickey took 42 minutes to finish the race.
    
    result = 42
    return result

print(solution())