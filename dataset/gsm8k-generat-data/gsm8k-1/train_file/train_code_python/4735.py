def solution():
    """A banana plantation on Jakies Island can produce ten times as many bananas as a banana plantation on a nearby island. If the banana plantation on the nearby island produced 9000 bananas in a year, what's the total banana produce from the two islands that year?"""
    
    bananas_nearby_island = 9000
    bananas_jakies_island = bananas_nearby_island * 10
    total_bananas = bananas_nearby_island + bananas_jakies_island
    result = total_bananas
    
    return result

print(solution())