def solution():
    shirt_iron_time = 5  # Minutes spent ironing his shirt
    pants_iron_time = 3  # Minutes spent ironing his pants
    days_per_week = 5  # Number of days per week he irons his clothes
    weeks = 4  # Number of weeks in a month

    # Calculate the total time spent ironing over 4 weeks
    total_iron_time = (shirt_iron_time + pants_iron_time) * days_per_week * weeks
    result = total_iron_time
    return result

print(solution())