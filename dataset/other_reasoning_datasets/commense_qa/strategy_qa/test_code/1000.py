def solution():
    NATO_members = ["country1", "country2", "country3"]  # replace with actual NATO countries
    nepal_flag = "double triangle"
    if nepal_flag == "double triangle" and "Nepal" not in NATO_members:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())