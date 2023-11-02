def solution():
    
    # Define the number of teeth James has
    james_teeth = 30

    # Calculate the number of teeth James's dentist drills
    dentist_drills = 4

    # Calculate the number of teeth James's dentist caps
    dentist_caps = james_drills + 7

    # Calculate the total number of teeth James has
    total_teeth = james_teeth - dentist_drills + dentist_caps

    # Calculate the percentage of teeth James' dentist fix
    dentist_percentage = (dentist_teeth / total_teeth) * 100

    # Display the percentage of teeth James' dentist fix
    result = dentist_percentage
    return result

print(solution())