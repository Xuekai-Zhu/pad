def solution():
    # Calculate the number of hoots per minute made by one barnyard owl
    hoots_per_owl = 5  
     
    # Find the total number of hoots per minute coming from the barn
    total_hoots = 20 - 5  # assuming 5 less than 20 hoots per minute are heard

    # Calculate the number of barnyard owls making the noise
    owls = total_hoots/hoots_per_owl
    result = owls
    return result

print(solution())