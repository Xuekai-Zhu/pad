def solution():
    fraktur_origin = "Germany"
    fraktur_use = ["official Nazi documents", "cover of Hitler's Mein Kampf"]
    if fraktur_origin == "Germany" and any(use in fraktur_use for use in ["Nazi documents", "Hitler's Mein Kampf"]):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())