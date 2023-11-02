def solution():
    time_from_ngapara_to_zipra = 60
    time_from_ningi_to_zipra = time_from_ngapara_to_zipra * 0.8  # 80% of time from Ngapara to Zipra
    
    total_time_traveled = time_from_ngapara_to_zipra + time_from_ningi_to_zipra
    result = total_time_traveled
    return result

print(solution())