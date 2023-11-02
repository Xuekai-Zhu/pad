def solution():
    japan_airlines_destinations = ["Germany", "Ireland", "Australia"]
    former_axis_powers = ["Germany", "Italy", "Japan"]
    overlap = [destination for destination in japan_airlines_destinations if destination in former_axis_powers]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())