def solution():
     Wednesday = 2
    Thursday = 3*Wednesday
    Friday=Thursday/2
     Weekend= 2*(Wednesday+Thursday+Friday)
     Total=Wednesday+Thursday+Friday+Weekend
     return Total

print(solution())