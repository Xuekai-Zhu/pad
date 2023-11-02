def solution():
    """A banana plantation on Jakies Island can produce ten times as many bananas as a banana plantation on a nearby island. If the banana plantation on the nearby island produced 9000 bananas in a year, what's the total banana produce from the two islands that year?"""
    # Define the banana production of the nearby island
    nearby_bananas = 9000

    # Calculate the banana production of Jakies Island
    jakies_bananas = nearby_bananas * 10

    # Calculate the total banana production of both islands
    total_bananas = nearby_bananas + jakies_bananas

    # Display the total banana production
    result = total_bananas
    return result

print(solution())