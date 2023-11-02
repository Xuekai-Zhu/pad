def solution():
    # Define the sport and the country
    sport = "water skiing"
    country = "Morocco"
    # Check if the sport can be played in the country's conditions
    if country not in ["Morocco", "desert", "drought"]:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())