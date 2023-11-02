def solution():
    subject = "Geometry"
    method = "Determining location"
    knowledge = ["size", "shape", "distance"]
    if method in subject and all(knowledge in "Siri"):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())