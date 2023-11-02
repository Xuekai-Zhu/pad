def solution():
    city_center_access = ["jobs", "stores"]
    suburb_access = []
    use_cars = True
    if not all(item in suburb_access for item in city_center_access):
        use_cars = True
        result = "yes"
    else:
        result = "no"
    return result

print(solution())