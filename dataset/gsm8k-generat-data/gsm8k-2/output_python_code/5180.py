def solution():
    """Jenny leaves her house at 8:00 with some cupcakes for her daughter's birthday party at school. She jogs to the school at 15 miles per hour. Half an hour later, her wife Anna realizes that Jenny used peanut butter frosting because she forgot one of the kids in the class had a severe peanut allergy. Jenny doesn't have her cell phone, so Anna leaves the house driving at 45 miles her hour to catch Jenny and warn her. How long does Anna spend traveling in minutes?"""
    jenny_speed = 15
    anna_speed = 45
    time_difference = 0.5  # in hours
    distance_jenny_covered = jenny_speed * time_difference
    total_distance = distance_jenny_covered
    anna_time = total_distance / anna_speed * 60  # in minutes
    result = anna_time
    return result

print(solution())