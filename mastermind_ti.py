import random
attempts = 0

def get_answer_ti():
    digits = [0,1,2,3,4,5,6,7,8,9]
    ans = []
    for i in range(4):
        ans.append(random.choice(digits))
        digits.remove(ans[len(ans)-1])
    return ans

def get_guess():
    global attempts
    while True:
        guess_in = input(': ')
        
        if guess_in.lower() not in ['exit', 'quit', 'close', 'end', 'reveal', 'show', 'give up']:
            # validation and formatting
            try:
                guess_in.split()
                guess_in = [int(digit) for digit in guess_in]
                if len(guess_in) == 4:
                    attempts += 1
                    return guess_in
                else:
                    print('your guess must be 4 digits')
            except:
                print('error')
        else:
            return 'end game'
            
def check(ans, guess):
    
    ans_used = [False] * 4
    guess_used = [False] * 4
    feedback = []
    
    # FIRST PASS - blacks
    for i in range(4):
        if ans[i] == guess[i]:
            ans_used[i] = guess_used[i] = True
            feedback.append('*')
        
    # SECOND PASS - whites
    for i in range(4):
        if not guess_used[i]:
            for j in range(4):
                if not ans_used[j] and guess[i] == ans[j]:
                    guess_used[i] = ans_used[j] = True
                    feedback.append('-')
                    break
        
    return ''.join(feedback)


# print instructions
print('''
Try to guess the 4-digit number
There are no repeated digits
You will get these hints:
* = a digit is in the right spot
- = a digit is in the wrong spot  
''')

# main gameplay loop
while True:

    ans = get_answer_ti()

    guess = get_guess()
    if guess == 'end game':
        print('the answer was ' + ''.join(str(digit) for digit in ans))
        quit()
    
    while guess != ans:
        print(check(ans, guess))
        print('')
        guess = get_guess()
        
    print('\nYOU WIN!')
    print('It took you ' + str(attempts) + ' attempts')  # do not use f-strings for ti
    break
