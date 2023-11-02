def solution():
    holy_cities = ["Ayodhya", "Mathura", "Haridwar", "Varanasi", "Kanchipuram", "Dvaraka", "Ujjain"]
    buddhist_site = "Bodh Gaya"
    shinto_shrine_location = "Ise"
    if holy_cities or buddhist_site or shinto_shrine_location:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())