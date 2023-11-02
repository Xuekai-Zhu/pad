def solution():
    """Jenny leaves her house at 8:00 with some cupcakes for her daughter's birthday party at school.
    She jogs to the school at 15 miles per hour. Half an hour later, her wife Anna realizes that Jenny used peanut butter
    frosting because she forgot one of the kids in the class had a severe peanut allergy.
    Jenny doesn't have her cell phone, so Anna leaves the house driving at 45 miles her hour to catch Jenny and warn her.
    How long does Anna spend traveling in minutes?"""
    # Define the distance from Jenny's house to the school in miles
    distance = 7

    # Calculate the time it takes Jenny to get to school in hours and convert it to minutes
    jenny_time = distance / 15 * 60

    # Calculate the time that Anna arrives at the house in minutes after 8:00
    anna_time = 8 * 60 + 30

    # Calculate the time it takes Anna to catch up to Jenny in minutes
    catch_up_time = distance / (45 - 15) * 60

    # Calculate the total time Anna spends traveling in minutes
    total_time = anna_time + catch_up_time - jenny_time

    # return the result
    result = round(total_time)
    return result

print(solution())