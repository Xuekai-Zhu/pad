def solution():
    total_time = 120  # The total time Miriam spent on tasks is 2 hours, or 120 minutes
    laundry_time = 30  # Miriam spent 30 minutes doing laundry
    bathroom_time = 15  # Miriam spent 15 minutes cleaning the bathroom
    homework_time = 40  # Miriam spent 40 minutes doing homework

    # Calculate the time Miriam spent cleaning her room
    room_time = total_time - laundry_time - bathroom_time - homework_time
    result = room_time
    return result

print(solution())