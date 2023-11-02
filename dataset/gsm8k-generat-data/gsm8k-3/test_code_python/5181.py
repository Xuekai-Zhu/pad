def solution():
    """Jenny leaves her house at 8:00 with some cupcakes for her daughter's birthday party at school. She jogs to the school at 15 miles per hour. Half an hour later, her wife Anna realizes that Jenny used peanut butter frosting because she forgot one of the kids in the class had a severe peanut allergy. Jenny doesn't have her cell phone, so Anna leaves the house driving at 45 miles her hour to catch Jenny and warn her. How long does Anna spend traveling in minutes?"""
    # Time taken by Jenny to reach the school
    time_taken_by_jenny = 0.5 + ((2 / 15) * 60)  # in minutes

    # Distance traveled by Jenny
    distance_traveled_by_jenny = (2 / 15)  # in miles

    # Time taken by Anna to catch Jenny
    time_taken_by_anna = distance_traveled_by_jenny / (45) * 60  # in minutes

    # Total time taken by Anna
    total_time_taken_by_anna = time_taken_by_jenny + time_taken_by_anna

    # Display the time taken by Anna
    result = total_time_taken_by_anna
    return result

print(solution())