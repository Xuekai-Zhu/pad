def solution():
    job_requirements = ["Ability to build physical constructs"]
    portfolio_requirements = ["Collection of items of a similar type"]
    if any(req in job_requirements for req in portfolio_requirements):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())