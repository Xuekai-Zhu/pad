def solution():
    """Jenny leaves her house at 8:00 with some cupcakes for her daughter's birthday party at school. She jogs to the school at 15 miles per hour. Half an hour later, her wife Anna realizes that Jenny used peanut butter frosting because she forgot one of the kids in the class had a severe peanut allergy. Jenny doesn't have her cell phone, so Anna leaves the house driving at 45 miles her hour to catch Jenny and warn her. How long does Anna spend traveling in minutes?"""
    jenny_speed = 15
    anna_speed = 45
    time_jenny = 0.5 + (2 / 15)
    distance_jenny = jenny_speed * time_jenny
    time_anna = distance_jenny / anna_speed * 60
    result = time_anna
    return result

print(solution())