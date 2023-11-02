def solution():
    distance = 480  # Joan wants to travel 480 miles
    speed = 60  # Joan drives at a speed of 60 mph
    lunch_break = 0.5  # Joan takes a 30-minute lunch break
    bathroom_breaks = 0.5  # Joan takes two 15-minute bathroom breaks

    # Calculate the time taken for the journey
    time_taken = distance / speed  # Time taken without breaks
    time_with_breaks = time_taken + lunch_break + bathroom_breaks  # Add break times to the total time

    result = time_with_breaks
    return result

print(solution())