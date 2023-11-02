def solution():
     
     tims_visit = 300
     insurance_coverage = 0.75
     tims_insurance_coverage = tims_visit * insurance_coverage
     tims_out_of_pocket = tims_visit - tims_insurance_coverage
     cats_visit = 120
     cats_insurance_coverage = 60
     cats_out_of_pocket = cats_visit - cats_insurance_coverage
     total_out_of_pocket = tims_out_of_pocket + cats_out_of_pocket
     result = total_out_of_pocket
     return result

print(solution())