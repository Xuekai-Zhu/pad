def solution():
     total_population = 300
     males_attending = 2 * females_attending
     total_attendees = males_attending + females_attending
     females_attending = total_attendees / 2
     result = females_attending
     return result

print(solution())