def solution():
    bobby_jindal_high_school = "Baton Rouge Magnet High School"
    high_school_mascot = "bulldog"
    food_type = "kibble"
    if high_school_mascot.lower() == "bulldog" and food_type.lower() == "kibble":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())