def solution():
    city_name = "Anaheim"
    city_founders = "German"
    founders_spoke_German = True
    founders_spoke_Italian = False
    if city_name == "Anaheim" and city_founders == "German" and not founders_spoke_Italian:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())