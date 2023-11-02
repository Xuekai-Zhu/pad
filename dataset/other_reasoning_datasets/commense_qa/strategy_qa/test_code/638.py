def solution():
    deafness_spectrum = ["total hearing loss", "partial hearing loss"]
    deaf_with_cochlear_implants = True
    if "total hearing loss" in deafness_spectrum or deaf_with_cochlear_implants:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())