def solution():
    # Create a list of the Star Wars TV shows produced by Disney
    disney_star_wars_shows = ["Star Wars Rebels", "Star Wars Resistance", "The Mandalorian", "Star Wars Clone Wars (revival season)"]
    # Check if there are multiple TV shows produced by Disney
    if len(disney_star_wars_shows) > 1:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())