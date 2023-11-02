def solution():
    has_tonsils = False
    has_had_tonsils_removed = True
    can_strep_grow_without_tonsils = True
    if not has_tonsils and has_had_tonsils_removed and can_strep_grow_without_tonsils:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())