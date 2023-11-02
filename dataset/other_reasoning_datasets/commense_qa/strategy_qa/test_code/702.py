def solution():
    peter_experience_years = "many"
    expected_knowledge_level = "familiar"
    if peter_experience_years == "many" and expected_knowledge_level == "expert":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())