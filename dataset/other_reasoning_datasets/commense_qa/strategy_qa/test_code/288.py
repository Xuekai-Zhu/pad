def solution():
    # Create a list of subjects a polymath would have knowledge in
    polymath_subjects = ["mathematics", "engineering", "computer science", "physics"]
    # Create a list of subjects Tony Stark has knowledge/skills in
    tony_stark_subjects = ["mathematics", "engineering", "computer science", "physics", "metalworking", "engine design", "genetics"]
    # Check if Tony Stark has knowledge/skills in all the subjects a polymath would have
    if set(polymath_subjects).issubset(set(tony_stark_subjects)):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())