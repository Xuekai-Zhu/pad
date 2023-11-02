def solution():
    gulf_properties = ["low salinity", "cold waters", "no shipworms"]
    titanic_origin = "British"
    if all(prop in gulf_properties for prop in ["low salinity", "cold waters", "no shipworms"]) and titanic_origin != "Finland":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())