def solution():
    
    flowers_planted = 125
    flowers_killed = {"red": 45, "yellow": 61, "orange": 30, "purple": 40}
    total_flowers = sum([flowers_planted - flowers_killed[color] for color in flowers_killed])
    bouquets_per_flower = total_flowers // 9
    result = bouquets_per_flower
    return result

print(solution())