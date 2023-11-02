def solution():
    """Pirate Rick sailed his ship to a tropical island in search of a site to bury his treasure. After finding the perfect site, it took him 4 hours to dig up 8 feet of sand under which to bury the treasure. Once the treasure was buried, he left the island. Then, a tropical storm came and washed away half of the sand from on top of the treasure. Next, a giant tsunami wave poured over the island, adding 2 feet of new sand back onto the site of his treasure. When Pirate Rick returned, how long did it take for him to dig up his treasure?"""
    initial_digging_time = 4
    initial_depth = 8
    storm_depth_reduction = initial_depth / 2
    tsunami_depth_addition = 2
    final_depth = initial_depth - storm_depth_reduction + tsunami_depth_addition
    digging_time = initial_digging_time * (final_depth / initial_depth)
    result = digging_time
    return result

print(solution())