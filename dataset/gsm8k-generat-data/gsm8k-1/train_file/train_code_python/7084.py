def solution():
    """A school is planning a community outreach program. Each classroom must raise $200 for this activity. Classroom A has raised $20 from each of two families, $10 from each of eight families, and $5 from each of ten families. How much more money does Classroom A need in order to reach the goal?"""
    goal = 200
    raised = (20*2) + (10*8) + (5*10)
    additional_needed = goal - raised
    result = additional_needed
    return result

print(solution())