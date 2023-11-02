def solution():
    """A banana plantation on Jakies Island can produce ten times as many bananas as a banana plantation on a nearby island. If the banana plantation on the nearby island produced 9000 bananas in a year, what's the total banana produce from the two islands that year?"""
    # Define the number of bananas produced by the nearby island
    nearby_bananas = 9000

    # Calculate the number of bananas produced by the Jakies Island plantation
    jakies_bananas = nearby_bananas * 10

    # Calculate the total banana produce from both islands
    total_bananas = nearby_bananas + jakies_bananas

    # return the result
    result = total_bananas
    return result

print(solution())