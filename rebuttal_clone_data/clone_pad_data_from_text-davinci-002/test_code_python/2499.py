def solution():
     loaves_morning = 2355
     loaves_sold = 629
     loaves_delivered = 489
     loaves_end = loaves_morning + loaves_delivered - loaves_sold
     result = loaves_end
     return result

print(solution())