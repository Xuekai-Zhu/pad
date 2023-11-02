def solution():
    cost_per_night = 40  # The cost per night per person is $40
    num_people = 3  # There are 3 people staying at the hotel
    num_nights = 3  # They stayed at the hotel for 3 nights

    # Calculate the total cost for all three people
    total_cost = cost_per_night * num_people * num_nights
    result = total_cost
    return result

print(solution())