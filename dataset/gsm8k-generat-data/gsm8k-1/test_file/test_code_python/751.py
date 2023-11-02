Unfortunately, a solution cannot be provided for the Samantha's last name question as it is incomplete and lacks necessary information. 

Defining a function for the Joey football question: 

def solution():
    """Joey plays football every week. Last week he played 2 matches on Monday, 
    1 match on Friday, and on Saturday he played double the number of matches he played on Monday. 
    How many matches did Joey play in one week?"""
    monday_matches = 2
    friday_matches = 1
    saturday_matches = monday_matches * 2
    total_matches = monday_matches + friday_matches + saturday_matches
    result = total_matches
    return result

print(solution())