def solution():
    tahiti_hotels = 47
    tahiti_rooms = 3000
    dday_troops = 23250 + 34250 + 15500
    
    if tahiti_rooms > dday_troops:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())