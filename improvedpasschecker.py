score = float(input('Enter a score from 0 to 100:'))
if score <0 or score >100:
    print('Invalid score. Input value between 0 and 100')
elif score >= 50:
    print('PASS!!')
else:
    print('fail')






score = float(input('Enter a Score from 0 to 100:'))
if 0 <= score <= 100: 
    print('The score is within valid range')
else:
    print('Invalid score')
 
