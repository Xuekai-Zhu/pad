def solution():
    # Calculate the number of pages Mack writes on Monday
    monday_pages = 60 // 30  # Mack writes 1 page every 30 minutes

    # Calculate the number of pages Mack writes on Tuesday
    tuesday_pages = 45 // 15  # Mack writes 1 page every 15 minutes

    # Calculate the total number of pages Mack writes from Monday to Wednesday
    total_pages = monday_pages + tuesday_pages + 5

    result = total_pages
    return result

print(solution())