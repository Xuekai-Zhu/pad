def solution():
    # Define the Forbidden City as an ancient historic site and wooden rollercoaster as a modern invention
    forbidden_city = "ancient historic site"
    wooden_rollercoaster = "modern invention"
    # Check if the Forbidden City is host to a wooden rollercoaster
    if wooden_rollercoaster not in forbidden_city:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())