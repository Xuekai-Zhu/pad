def solution():
    # Define the speeds of Susan and Tracy in terms of x
    susan_speed = x
    pete_backward_speed = 3*x
    tracy_speed = 2*x

    # Use the given information to create equations
    pete_hand_speed = 0.25 * tracy_speed
    pete_hand_speed = 2  # given
    tracy_speed = 8  # solve for Tracy's speed

    # Solve for x and then for Pete's backward speed
    x = tracy_speed / 2
    pete_backward_speed = 3*x

    result = pete_backward_speed
    return result

print(solution())