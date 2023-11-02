def solution():
    driver_education_classes_offered = True
    driving_test_required = True
    eleventh_grade_enrollment = False # assumption based on the information provided
    if driver_education_classes_offered and driving_test_required and eleventh_grade_enrollment:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())