def solution():
     total_envelopes = 1500
     envelopes_stuffed_1 = 135
     envelopes_stuffed_2 = 141
     envelopes_stuffed_per_hour = (total_envelopes - (envelopes_stuffed_1 + envelopes_stuffed_2)) / 6
     result = envelopes_stuffed_per_hour
     return result

print(solution())