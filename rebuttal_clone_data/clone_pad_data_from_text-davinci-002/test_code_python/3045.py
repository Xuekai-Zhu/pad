def solution():
     total_rolls = 30
     tickets_per_roll = 100
     fourth_grader_percent = 30
     fifth_grader_percent = 50
     sixth_grader_percent = 100
     fourth_grader_tickets = total_rolls * tickets_per_roll * (fourth_grader_percent / 100)
     fifth_grader_tickets = total_rolls * tickets_per_roll * (fifth_grader_percent / 100)
     sixth_grader_tickets = total_rolls * tickets_per_roll * (sixth_grader_percent / 100)
     total_ sold = fourth_grader_tickets + fifth_grader_tickets + sixth_grader_tickets
     total_tickets = total_rolls * tickets_per_roll
     unsold_tickets = total_tickets - total_sold
     result = unsold_tickets
     return result

print(solution())