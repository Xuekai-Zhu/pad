def solution():
    """Tommy is making steaks for his family. There are 5 of them in total. If each member wants one pound and the steaks are 20 ounces each, how many does he need to buy?"""
    # Define the number of people and the desired weight per person
    num_people = 5
    weight_per_person = 16  # 1 pound = 16 ounces

    # Calculate the total weight needed
    total_weight = num_people * weight_per_person

    # Calculate the number of steaks needed
    steak_weight = 20  # ounces per steak
    num_steaks = total_weight / steak_weight

    # Round up to the nearest whole number of steaks
    num_steaks = int(round(num_steaks))

    # Display the number of steaks needed
    result = num_steaks
    return result

print(solution())