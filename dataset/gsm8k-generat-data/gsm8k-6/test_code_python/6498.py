def solution():
    # Calculate the total number of pages read by DeShaun
    total_pages = 60 * 320  

    # Calculate the number of pages read by the second person
    second_person_pages = total_pages * 0.75  

    # Calculate the average number of pages read per day by the second person
    pages_per_day = second_person_pages / 80  
    result = pages_per_day
    return result

print(solution())