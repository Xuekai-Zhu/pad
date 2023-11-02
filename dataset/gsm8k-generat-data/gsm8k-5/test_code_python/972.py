def solution():
    current_floor = 9    # The elevator starts at the 9th floor
    current_floor -= 7   # The elevator goes down 7 floors
    current_floor += 3   # The elevator goes up 3 floors
    current_floor += 8   # The elevator goes up 8 floors to reach the top floor

    total_floors = current_floor   # The total number of floors is the current floor the elevator is on

    result = total_floors
    return result

print(solution())