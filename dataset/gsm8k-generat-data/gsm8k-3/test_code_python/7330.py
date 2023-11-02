def solution():
    """Pirate Rick sailed his ship to a tropical island in search of a site to bury his treasure. After finding the perfect site, it took him 4 hours to dig up 8 feet of sand under which to bury the treasure. Once the treasure was buried, he left the island. Then, a tropical storm came and washed away half of the sand from on top of the treasure. Next, a giant tsunami wave poured over the island, adding 2 feet of new sand back onto the site of his treasure. When Pirate Rick returned, how long did it take for him to dig up his treasure?"""
    # Calculate the amount of sand covering the treasure after the storm and tsunami
    sand_covering = (8 / 2) + 2

    # Calculate the time it would take to dig up the treasure
    time_to_dig = 4 * (8 + sand_covering) / 8

    # Display the time it would take to dig up the treasure
    result = time_to_dig
    return result

print(solution())