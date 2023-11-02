def solution():
    """Jason, Ryan, and Jeffery went fishing at the lake. Ryan caught three times the number of fish that Jason caught. Jefferey caught twice the number of fish that Ryan got. If Jeffery caught 60 fish, how many fish did all of them catch in total?"""
    jeffery_fish = 60
    ryan_fish = jeffery_fish / 2
    jason_fish = ryan_fish / 3
    total_fish = jeffery_fish + ryan_fish + jason_fish
    result = total_fish
    return result

print(solution())