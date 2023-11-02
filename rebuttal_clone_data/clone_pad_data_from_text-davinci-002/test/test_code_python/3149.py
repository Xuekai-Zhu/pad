def solution():
     percent_voting_for_biff = 45
     percent_undecided = 8
     percent_voting_for_marty = 100 - (percent_voting_for_biff + percent_undecided)
     people_polled = 200
     people_voting_for_marty = people_polled * (percent_voting_for_marty / 100)
     result = people_voting_for_marty
     return result

print(solution())