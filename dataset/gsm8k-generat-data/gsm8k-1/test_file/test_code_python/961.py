def solution():
    """A bird decides to leave her summer home in the north and travel to her winter home in the south. To make the journey, the bird leaves her home flying in a southerly direction for 10 hours at a speed of 30 miles per hour. Then, the bird turns direction and flies towards the north for 2 hours are a speed of 18 miles per hour. Finally, the bird changes direction and flies toward the south for 5 hours at a speed of 22 miles per hour before landing at her southern home. What is the distance, in miles, between the bird's northern and the southern homes?"""
    
    distance_south = 10 * 30 # distance covered when flying towards the south
    distance_north = 2 * 18 # distance covered when flying towards the north
    distance_south_again = 5 * 22 # distance covered when flying towards the south again
    
    total_distance = distance_south + distance_north + distance_south_again
    
    return total_distance

print(solution())