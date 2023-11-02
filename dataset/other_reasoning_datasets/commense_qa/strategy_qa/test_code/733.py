def solution():
    therapist_bound_by_confidentiality = True
    acknowledgement_of_clients_outside_therapy_violates_APA_standard = True
    if therapist_bound_by_confidentiality and acknowledgement_of_clients_outside_therapy_violates_APA_standard:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())