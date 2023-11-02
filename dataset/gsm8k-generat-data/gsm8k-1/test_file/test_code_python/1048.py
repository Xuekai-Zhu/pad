def solution():
    """Romeo boards a train with 120 people. At the first stop, 20 more people board the train. At the second stop, 50 people descended from the train while twice that number boarded the train. If 80 more people descended at the third station, calculate the total number of people on the train at the final stop."""
    initial_passengers = 120
    first_stop_passengers = initial_passengers + 20
    second_stop_passengers = first_stop_passengers - 50 + (2*50)
    final_passengers = second_stop_passengers - 80
    result = final_passengers
    return result

print(solution())