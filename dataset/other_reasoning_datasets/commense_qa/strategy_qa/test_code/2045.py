def solution():
    industry = ["beverage"]
    required_jobs = ["cooper"]
    overlap = [job for job in required_jobs if job in industry]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())