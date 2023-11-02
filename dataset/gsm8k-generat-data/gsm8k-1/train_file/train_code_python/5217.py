def solution():
    """Brian goes fishing twice as often as Chris, but catches 2/5 times fewer fish than Chris per trip. If Brian caught 400 fish every time he went fishing, how many fish did they catch altogether if Chris went fishing 10 times?"""
    brian_fishing_frequency = 2
    chris_fishing_frequency = 1
    chris_fish_per_trip = 500
    brian_fish_per_trip = (3 / 5) * chris_fish_per_trip
    brian_total_fish = brian_fishing_frequency * 400
    chris_total_fish = chris_fishing_frequency * chris_fish_per_trip * 10
    total_fish = brian_total_fish + chris_total_fish
    result = total_fish
    return result

print(solution())