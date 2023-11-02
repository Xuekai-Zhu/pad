def solution():
    """Tomorrow, 42 adults and 15 babies will be attending a function at Mia’s restaurant. The restaurant has 5 times as many regular chairs as high chairs. If there are 8 high chairs, how many more chairs does she have to get?"""
    adults = 42
    babies = 15
    high_chairs = 8
    regular_chairs = 5 * high_chairs
    total_chairs_needed = adults + babies + high_chairs
    chairs_to_get = total_chairs_needed - (high_chairs + regular_chairs)
    result = chairs_to_get
    return result

print(solution())