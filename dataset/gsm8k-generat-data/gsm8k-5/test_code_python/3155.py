def solution():
    total_bars = 200
    num_people = 5
    
    # Calculate the number of bars taken by Thomas and his friends
    num_bars_taken = (1/4) * total_bars
    num_bars_per_person = num_bars_taken / num_people

    # One friend returns 5 bars
    num_bars_returned = 5
    num_bars_taken -= num_bars_returned
    num_people -= 1

    # Calculate the number of bars taken by Piper
    num_bars_taken += num_bars_returned - 5

    # Calculate the total number of bars left in the box
    num_bars_left = total_bars - num_bars_taken
    result = num_bars_left
    return result

print(solution())