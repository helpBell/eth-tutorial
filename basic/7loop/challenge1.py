item = 0
dan = 10
while item < 10:
    if(dan > 9):
        dan = 1
        item += 1
        if(item < 10):
            print(f'{item}단')
    else:    
        print(f'{dan}*{item} = {dan*item}')
        dan += 1 