def solution():
    """Ricky has 40 roses. His little sister steals 4 roses. If he wants to give away the rest of the roses in equal portions to 9 different people, how many roses will each person get?"""
    # Define the initial number of roses
    initial_roses = 40

    # Define the number of roses stolen by Ricky's sister
    stolen_roses = 4

    # Calculate the number of remaining roses
    remaining_roses = initial_roses - stolen_roses

    # Calculate the number of roses each person will receive
    per_person_roses = remaining_roses // 9

    # Return the result
    result = per_person_roses
    return result

print(solution())