ph = int(input('Enter PH level:'))

if ph < 0 or ph > 14:
    print('Invalid PH level')
    print('Please enter a PH level between 0 and 14')

elif ph > 7:
    print('PH is Basic')

elif ph < 7:
    print('PH is Acidic')

else:
    print('PH is Neutral')
