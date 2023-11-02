def solution():
    headquarters_city = "Geneva"
    famous_foods = ["Raclette"]
    if "Raclette" in famous_foods and headquarters_city == "Geneva":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())