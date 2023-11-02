def solution():
    communist_ideology = "foundation of communist party of China"
    marx_influence = "communist manifesto"
    if marx_influence in communist_ideology:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())