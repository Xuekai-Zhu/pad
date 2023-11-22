def solution():
    
    # Define the number of wolves and cougars killed last night
    last_night_wolves = 10
    last_night_cougars = 15

    # Calculate the number of wolves and cougars killed today
    today_wolves = last_night_wolves * 3
    today_cougars = last_night_cougars - 3

    # Calculate the total number of animals killed
    total_animals = last_night_wolves + last_night_cougars + today_wolves + today_cougars

    # Display the total number of animals killed
    result = total_animals
    return result

print(solution())