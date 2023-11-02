def solution():
     times_hiked_camila = 7
     times_hiked_amanda = times_hiked_camila * 8
     times_hiked_steven = times_hiked_amanda + 15
     times_hiked_goal = times_hiked_steven
     hikes_per_week = 4
     weeks_to_hike = times_hiked_goal / hikes_per_week
     result = weeks_to_hike
     return result

print(solution())