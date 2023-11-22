def solution():
    
    # Define the initial number of teeth
    initial_teeth = 30

    # Calculate the number of teeth that James' dentist drills
    dentist_drills = 4

    # Calculate the number of teeth that James' dentist caps
    dentist_caps = dentist_drills + 7

    # Calculate the total number of teeth that the dentist has
    total_dentist_teeth = dentist_drills + dentist_caps

    # Calculate the percentage of teeth that the dentist fix
    dentist_fix_percentage = (dentist_drills / initial_teeth) * 100

    # Display the percentage of teeth that the dentist fix
    result = dentist_fix_percentage
    return result

print(solution())