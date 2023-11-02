def solution():
    # Define the job requirements for working at UPS and the qualifications of Iris and Hermes
    job_requirements = ["delivery/courier service", "emissary/messenger"]
    iris_qualifications = ["messenger of the gods"]
    hermes_qualifications = ["emissary and messenger of the gods"]
    # Check if Iris and Hermes meet the job requirements
    if all(requirement in iris_qualifications + hermes_qualifications for requirement in job_requirements):
        result = "no"
    else:
        result = "yes"
    return result

print(solution())