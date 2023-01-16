numbers=[1,3,5]
position=0
while position <len(numbers):
    number = numbers[position]
    if number %2 == 0:
        print('짝수 찾음', number)
        break
    position+=1
else:
    print('짝수 없음.')




