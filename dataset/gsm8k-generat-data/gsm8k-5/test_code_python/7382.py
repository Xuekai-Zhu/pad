def solution():
    total_members = 5  # There are 5 people in Tommy's family
    weight_per_person = 1  # Each person wants 1 pound of steak
    weight_per_steak = 20/16  # Each steak weighs 20 ounces, which is 1.25 pounds

    # Calculate the total weight of steak needed
    total_weight = total_members * weight_per_person

    # Calculate the total number of steaks Tommy needs to buy
    total_steaks = total_weight / weight_per_steak
    result = total_steaks
    return result

print(solution())