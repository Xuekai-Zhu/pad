def solution():
    allowed_foods = ["anything except beef"]
    prohibited_foods = ["beef"]
    if "crustacean" in allowed_foods and "crustacean" not in prohibited_foods:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())