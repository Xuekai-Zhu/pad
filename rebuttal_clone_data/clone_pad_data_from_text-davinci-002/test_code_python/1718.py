def solution():
    fish_caught_pelican = 13
    fish_caught_kingfisher = fish_caught_pelican + 7
    total_fish_caught = fish_caught_pelican + fish_caught_kingfisher
    fish_caught_fisherman = total_fish_caught * 3
    fish_caught_difference = fish_caught_fisherman - total_fish_caught
    result = fish_caught_difference
    
    return result

print(solution())