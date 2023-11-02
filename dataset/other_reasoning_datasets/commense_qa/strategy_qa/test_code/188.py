def solution():
    skype_founders = ["Niklas Zennström", "Janus Friis"]
    asian_countries = ["Asia"]
    founders_origin = "Europe"
    if founders_origin not in asian_countries:
        result = "no"
    else:
        asian_founders = [founder for founder in skype_founders if founder in asian_countries]
        if asian_founders:
            result = "yes"
        else:
            result = "no"
    return result

print(solution())