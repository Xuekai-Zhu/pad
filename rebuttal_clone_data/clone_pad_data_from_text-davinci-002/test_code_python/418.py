def solution():
     total_pencils = 50
     pencils_to_manny = 10
     pencils_to_nilo = pencils_to_manny + 10
     pencils_kept = total_pencils - pencils_to_manny - pencils_to_nilo
     result = pencils_kept
     return result

print(solution())