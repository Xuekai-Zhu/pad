def solution():
    """A banana plantation on Jakies Island can produce ten times as many bananas as a banana plantation on a nearby island. If the banana plantation on the nearby island produced 9000 bananas in a year, what's the total banana produce from the two islands that year?"""
    nearby_bananas = 9000
    jakies_bananas = 10 * nearby_bananas
    total_bananas = nearby_bananas + jakies_bananas
    result = total_bananas
    return result

print(solution())