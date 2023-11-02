def solution():
    
    rolls = 30
    tickets_per_roll = 100
    total_tickets = rolls * tickets_per_roll
    fourth_graders = int(total_tickets * 0.3)
    remaining_tickets = total_tickets - fourth_graders
    fifth_graders = int(remaining_tickets * 0.5)
    remaining_tickets -= fifth_graders
    sixth_graders = 100
    remaining_tickets -= sixth_graders
    result = remaining_tickets
    return result

print(solution())