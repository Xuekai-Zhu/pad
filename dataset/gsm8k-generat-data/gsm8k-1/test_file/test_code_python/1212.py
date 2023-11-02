def solution():
    """A bus has a capacity of 200 people. 
    When it departed Chengli city, it had 20 people. 
    On the first stop, 40 people entered the bus. 
    On the second station, 3/4 of the total number of people who entered the bus at the first station entered the bus. 
    If the number of passengers on the bus doubled at the third station, calculate the total number of people required to fill the remaining spaces on the bus."""
    
    capacity = 200
    current_passengers = 20
    current_passengers += 40  # passengers at first stop
    current_passengers += (3/4)*40  # passengers at second stop
    current_passengers *= 2  # passengers at third stop
    
    remaining_spaces = capacity - current_passengers
    result = remaining_spaces
    
    return result

print(solution())