def solution():
    num_humans = 38e6
    
    # Calculate the number of beavers based on the human population
    num_beavers = num_humans / 19

    # Calculate the number of moose based on the beaver population
    num_moose = num_beavers / 2

    # Convert the moose population to millions and round to 2 decimal places
    result = round(num_moose / 1e6, 2)
    return result

print(solution())