def solution():
    
    # Define the number of bottles per case of water
    BOTTLES_PER_CASE = 24

    # Define the number of cases of water Bill started with
    cases_of_water = 2

    # Define the number of guests Bill will be arriving
    guests = 70

    # Define the number of bottles of water Bill wants to buy for each guest
    bottles_per_guest = 2

    # Calculate the total number of bottles of water Bill will buy
    total_bottles = cases_of_water * BOTTLES_PER_CASE + guests * bottles_per_guest

    # Calculate the number of additional bottles of water Bill needs to buy
    additional_bottles = total_bottles - total_bottles

    # Display the number of additional bottles of water Bill needs to buy
    result = additional_bottles
    return result

print(solution())