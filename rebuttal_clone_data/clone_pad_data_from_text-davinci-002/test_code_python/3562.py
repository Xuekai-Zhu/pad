def solution():
     cj_total = 930
     kj_total = 930
     aj_total = 930
     
     cj_stamp = 2*5 + kj_stamp
     kj_stamp = aj_stamp/2
     aj_stamp = cj_total - kj_total - aj_total
     
     return aj_stamp

print(solution())