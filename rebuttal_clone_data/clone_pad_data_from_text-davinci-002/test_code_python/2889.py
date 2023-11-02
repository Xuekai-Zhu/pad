def solution():
    total_guests = 200
    percent_yes = 83
    percent_no = 9
    guests_yes = total_guests * (percent_yes / 100)
    guests_no = total_guests * (percent_no / 100)
    guests_not_responding = total_guests - (guests_yes + guests_no)
    result = guests_not_responding
    
    return result

print(solution())