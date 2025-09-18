import random
attempts = 0

# ANSI colors
bg_green = '\033[42m'
bg_yellow = '\033[43m'
bg_none = '\033[49m'
fg_blue = '\033[34m'
fg_green = '\033[32m'
fg_yellow = '\033[33m'
fg_red = '\033[31m'
fg_none = '\033[39m'

def get_answer_pc():
    return(random.sample(range(0,10),4))

def get_guess(ans):
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
                    print(f'{fg_red}your guess must be 4 digits{fg_none}')
            except:
                print(f'{fg_red}error{fg_none}')
        else:
            ans_disp = ''.join(str(digit) for digit in ans)
            print(f'The answer was {ans_disp}')
            quit()
            
def check(ans, guess):
    
    ans_used = [False] * 4
    guess_used = [False] * 4
    feedback = []
    
    # FIRST PASS - blacks
    for i in range(4):
        if ans[i] == guess[i]:
            ans_used[i] = guess_used[i] = True
            feedback.append(f'{fg_green} {fg_none}')
        
    # SECOND PASS - whites
    for i in range(4):
        if not guess_used[i]:
            for j in range(4):
                if not ans_used[j] and guess[i] == ans[j]:
                    guess_used[i] = ans_used[j] = True
                    feedback.append(f'{fg_yellow}󰍶 {fg_none}')
                    break
        
    return ''.join(feedback)


# print instructions
print(f'''
Try to guess the 4-digit number
There are no repeated digits
You will get these hints:
{fg_green}{bg_green}{fg_none}✓ = a digit is in the right spot{bg_none}{fg_green}
{fg_yellow}{bg_yellow}{fg_none}– = a digit is in the wrong spot{bg_none}{fg_yellow}{fg_none}
''')

# main gameplay loop
while True:

    ans = get_answer_pc()

    guess = get_guess(ans)
    
    while guess != ans:
        print(check(ans, guess))
        print('')
        guess = get_guess(ans)
        
    print(f'\n\033[34mYOU WIN! 󱁖')
    print(f'It took you {str(attempts)} attempts')
    break
