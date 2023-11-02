def solution():
    distance = 20 + 200  # Rich walks 20 feet from his house and 200 feet down the sidewalk to the end of the road
    distance *= 2  # Rich walks double his total distance from the start until he reaches the next intersection
    distance += 20 + 200  # Rich walks another 20 feet from the intersection to the end of his route, then turns around and walks the same path back home
    distance *= 2  # Rich walks the same path back home

    result = distance
    return result

print(solution())