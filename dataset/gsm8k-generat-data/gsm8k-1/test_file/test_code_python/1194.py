def solution():
    """To participate in the local community tree-planting campaign, Mr. Julius planted twenty trees of White Oak and twice as many Lodgepole Pine as White Oak on his first day. On the second day, he planted 10 more White Oak trees and 1/4 more Lodgepole Pine trees than he planted on the first day. Calculate the total number of trees planted by Mr. Julius in the two days."""
    white_oak_day1 = 20
    lodgepole_pine_day1 = white_oak_day1 * 2
    white_oak_day2 = white_oak_day1 + 10
    lodgepole_pine_day2 = int(lodgepole_pine_day1 * 1.25)
    total_trees_planted = white_oak_day1 + lodgepole_pine_day1 + white_oak_day2 + lodgepole_pine_day2
    result = total_trees_planted
    return result

print(solution())