def solution():
    dale_sr_death_cause = "Basilar skull fracture"
    did_dale_sr_crash_due_to_stroke = False
    if dale_sr_death_cause == "Basilar skull fracture" and not did_dale_sr_crash_due_to_stroke:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())