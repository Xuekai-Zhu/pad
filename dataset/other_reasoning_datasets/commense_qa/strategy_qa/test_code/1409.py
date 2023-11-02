def solution():
    holiday = "Passover"
    seder_items = ["bitter herb"]
    bitter_herb = "horseradish"
    
    if holiday == "Passover" and bitter_herb in seder_items:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())