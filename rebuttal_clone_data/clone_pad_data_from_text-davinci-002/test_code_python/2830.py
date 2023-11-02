def solution():
    n=12
    x=2
    Derek_save=0
    for i in range(1,n+1):
        Derek_save+=x
        x*=2
    return Derek_save

print(solution())