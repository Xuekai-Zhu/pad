def solution():
     total_score = 50 * 2
     marks_lost = 20
     friend_a_score = total_score - marks_lost
     marks_gained = 40
     friend_b_score = friend_a_score + marks_gained
     questions_wrong = 5
     marks_deducted = questions_wrong * 2
     friend_c_score = friend_b_score - marks_deducted
     result = friend_a_score + friend_b_score + friend_c_score
     return result

print(solution())