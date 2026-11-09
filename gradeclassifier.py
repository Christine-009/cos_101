name = (input('Enter name:'))
score = float(input('Enter Score:'))
if score < 0 or score >100:
    print('Invalid score. Input appropriate value')
else:
    if score >=70:
        grade = 'A'
    elif score >=60:
        grade = 'B'
    elif score >=50:
        grade = 'C'
    elif score >=45:
        grade = 'D'
    elif score >=40:
        grade = 'E'
    elif score < 40:
        grade = 'F'

    print()
    print('STUDENT PROFILE')
    print(f'Name: {name}')
    print(f'Score: {score:.2f}')
    print(f'Grade: {grade}')
    print('Result Checking Completed')
