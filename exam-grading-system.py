HW = '25'
ASS = '50'
FE = '100'
OVERALL = '175'

def percent(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    percentage = (num1 / num2 * 100)
    return percentage

print('-----------------------------------------------------------')

student_name = str(input('Enter student name:   '))

HWM = int(input('Please enter Homework mark:   '))

ASSM = int(input('Please enter Assessment mark:   '))

FEM = int(input('Please enter Final exam mark:   '))

print('-----------------------------------------------------------')

HWM_per = percent(HWM, HW)

ASSM_per = percent(ASSM, ASS)

FEM_per = percent(FEM, FE)

overall = (HWM + ASSM + FEM)

Grade = percent(overall, OVERALL)

if Grade >= 80:
    print('Student name = ', student_name,
          '\nHomework =', HWM_per,
          '\nAssesment mark =', ASSM_per,
          '\nFinal Exam =', FEM_per,
          '\nOverall Grade = A\n Amazing!')
    

elif Grade >= 70:
    print('Student = ', student_name,
          '\nHomework =', HWM_per,
          '\nAssesment mark =', ASSM_per,
          '\nFinal Exam =', FEM_per,
          '\nOverall Grade = B\n Great!')
    
    
elif Grade >= 60:
    print('Student = ', student_name,
          '\nHomework =', HWM_per,
          '\nAssesment mark =', ASSM_per,
          '\nFinal Exam =', FEM_per,
          '\nOverall Grade = C\n Almost!')
    

elif Grade >= 50:
    print('Student = ', student_name,
          '\nHomework =', HWM_per,
          '\nAssesment mark =', ASSM_per,
          '\nFinal Exam =', FEM_per,
          '\nOverall Grade = D\n Better luck next time!')
    

elif Grade >= 40:
    print('Student = ', student_name,
          '\nHomework =', HWM_per,
          '\nAssesment mark =', ASSM_per,
          '\nFinal Exam =', FEM_per,
          '\nOverall Grade = E\n Too bad!')
    

elif Grade <= 39:
    print('Student = ', student_name,
          '\nHomework =', HWM_per,
          '\nAssesment mark =', ASSM_per,
          '\nFinal Exam =', FEM_per,
          '\nOverall Grade = F\n Really!?')
    





