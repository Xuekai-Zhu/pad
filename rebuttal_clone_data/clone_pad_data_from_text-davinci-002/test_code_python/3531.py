def solution():
     Nigel_won = 45
     Nigel_given = 10
     Nigel_double = Nigel_won * 2
     Nigel_total = Nigel_won + Nigel_given + Nigel_double
     Nigel_given_away = Nigel_total - Nigel_double
 
     return Nigel_given_away

print(solution())