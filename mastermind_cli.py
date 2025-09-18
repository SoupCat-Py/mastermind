import random
attempts = 0

# ANSI colors
def style(fg='fgnone', bg='bgnone',):
    fg_dict = {'fgblue': 34, 'fggreen' : 32, 'fgyellow' : 33, 'fgred' : 31, 'fgnone' : 39}
    bg_dict = {'bggreen' : 42, 'bgyellow' : 43, 'bgnone' : 49}
    return f'\033[{str(fg_dict[fg])};{str(bg_dict[bg])}m'

def get_answer_cli():
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
                    print(f'{style("fgred")}your guess must be 4 digits{style()}')
            except:
                print(f'{style("fgred")}error{style()}')
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
            feedback.append(f'{style("fggreen")} {style()}')
        
    # SECOND PASS - whites
    for i in range(4):
        if not guess_used[i]:
            for j in range(4):
                if not ans_used[j] and guess[i] == ans[j]:
                    guess_used[i] = ans_used[j] = True
                    feedback.append(f'{style("fgyellow")}󰍶 {style()}')
                    break
        
    return ''.join(feedback)


# print instructions
print(f'''
Try to guess the 4-digit number
There are no repeated digits
You will get these hints:
{style("fggreen")}{style("fgnone","bggreen")}✓ = a digit is in the right spot{style("fggreen")}
{style("fgyellow")}{style("fgnone","bgyellow")}– = a digit is in the wrong spot{style("fgyellow")}{style()}
''')

# main gameplay loop
while True:

    ans = get_answer_cli()

    guess = get_guess(ans)
    
    while guess != ans:
        print(check(ans, guess))
        print('')
        guess = get_guess(ans)
        
    print(f'\n{style("fgblue")}\033[5mYOU WIN! 󱁖\033[25m')  # blinking only works in select terminals
    print(f'It took you {str(attempts)} attempts')
    break
