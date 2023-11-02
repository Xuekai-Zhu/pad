def solution():
    # Define the number of starting tourists and the number eaten by anacondas
    starting_tourists = 30
    anaconda_victims = 2

    # Calculate the number of remaining tourists
    remaining_tourists = starting_tourists - anaconda_victims

    # Calculate the number of tourists poisoned by dart frogs
    dart_frog_victims = remaining_tourists // 2

    # Calculate the number of tourists who recovered from the poison
    recovered_victims = dart_frog_victims // 7

    # Calculate the final number of tourists
    final_tourists = remaining_tourists - dart_frog_victims + recovered_victims

    result = final_tourists
    return result

print(solution())