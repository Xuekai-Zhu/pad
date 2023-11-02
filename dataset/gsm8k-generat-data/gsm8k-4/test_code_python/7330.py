def solution():
    """Pirate Rick sailed his ship to a tropical island in search of a site to bury his treasure. After finding the perfect site, it took him 4 hours to dig up 8 feet of sand under which to bury the treasure. Once the treasure was buried, he left the island. Then, a tropical storm came and washed away half of the sand from on top of the treasure. Next, a giant tsunami wave poured over the island, adding 2 feet of new sand back onto the site of his treasure. When Pirate Rick returned, how long did it take for him to dig up his treasure?"""
    
    # Define the initial depth of sand
    initial_depth = 8

    # Calculate the depth of sand after the storm
    depth_after_storm = initial_depth / 2

    # Calculate the depth of sand after the tsunami
    depth_after_tsunami = depth_after_storm + 2

    # Calculate the total depth of sand that needs to be dug up
    total_depth = initial_depth - depth_after_tsunami

    # Calculate the time it takes to dig up the treasure
    time = total_depth / 8

    # Return the result
    result = time
    return result

print(solution())