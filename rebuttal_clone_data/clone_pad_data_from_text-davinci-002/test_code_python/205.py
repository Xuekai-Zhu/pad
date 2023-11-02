def solution():
     """Wickham is throwing a huge Christmas party. He invites 30 people. Everyone attends the party, and half of the guests bring a plus one (one other person). He plans to serve a 3-course meal for the guests. If he uses a new plate for every course, how many plates does he need in total for his guests?"""
     people_invited = 30
     guests_attending = people_invited * 2
     courses = 3
     plates_needed = guests_attending * courses
     result = plates_needed
     return result

print(solution())