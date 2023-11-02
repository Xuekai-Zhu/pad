def solution():
    """Suzanne wants to raise money for charity by running a 5-kilometer race. Her parents have pledged to donate $10 for her first kilometer and double the donation for every successive kilometer. If Suzanne finishes the race, how much money will her parents donate?"""
    # Define the initial donation amount and the total donation amount
    initial_donation = 10
    total_donation = initial_donation

    # Calculate the donation for each of the remaining kilometers
    for kilometer in range(2, 6):
        donation = initial_donation * 2 ** (kilometer - 1)
        total_donation += donation

    # return the total donation amount
    result = total_donation
    return result

print(solution())