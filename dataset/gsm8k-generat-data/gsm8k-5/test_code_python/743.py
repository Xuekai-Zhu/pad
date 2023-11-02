def solution():
    gallons_per_mile = 20  # Empty plane needs 20 gallons of fuel per mile
    total_people = 30 + 5  # 30 passengers and 5 flight crew
    total_bags = 30 * 2  # each person brought two bags

    # Calculate the additional gallons of fuel needed for people and bags
    additional_gallons_per_mile = (3 * total_people) + (2 * total_bags)

    # Calculate the total gallons of fuel needed for the trip
    total_gallons = gallons_per_mile * 400 + additional_gallons_per_mile * 400

    result = total_gallons
    return result

print(solution())