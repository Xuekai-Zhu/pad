def solution():
     days_of_week = 7
     days_eating = 5
     days_not_eating = days_of_week - days_eating
     number_of_weeks = 3
     total_number_of_candy = number_of_weeks * (days_eating * 2 + days_not_eating)
     candies_per_packet = total_number_of_candy / 2
     result = candies_per_packet
     return result

print(solution())