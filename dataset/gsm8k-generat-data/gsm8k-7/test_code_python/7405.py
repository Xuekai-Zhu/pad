def solution():
    total_money = 60
    frame_cost = 15
    front_wheel_cost = 25

    # Calculate the total amount spent on the frame and front wheel
    total_spent = frame_cost + front_wheel_cost

    # Calculate the amount left for the seat and handlebar tape
    amount_left = total_money - total_spent
    result = amount_left
    return result

print(solution())