def solution():
    # Define the probability of packing a peanut butter sandwich
    pb_probability = 2/5

    # Define the probability of packing a ham sandwich
    ham_probability = 3/5

    # Define the probability of packing cake
    cake_probability = 1/5

    # Define the probability of packing cookies
    cookie_probability = 4/5

    # Calculate the probability of packing a ham sandwich and cake on the same day
    ham_cake_probability = ham_probability * cake_probability

    # Convert the probability to a percentage
    result = ham_cake_probability * 100
    return result

print(solution())