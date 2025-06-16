import random
MAX_LINES=3
MAX_BET=100
MIN_BET=1
ROWS=3
COLS=3

symbol_count={
    'A':2,
    'B':4,
    'C':6,
    'D':8
}
symbol_value={
    'A':5,
    'B':4,
    'C':3,
    'D':2
}
# Deposit of Money.
def deposit():
    while True:
        user_amount=input('Enter the deposit amount:')
        if user_amount.isdigit():
            user_amount=int(user_amount)
            if user_amount > 0:
                return user_amount
            else:
                print('Enter valid amount.')
        else:
            print('Enter a valid number.')

# Number of lines user wants to bet on.
def no_of_line():
    while True:
        lines=input('Enter how many lines to bet on(1-'+ str(MAX_LINES) +')?')
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINES:
                return lines
            else:
                print('Enter a valid number')
        else:
            print('Enter the line number.')


# Ask user to put the bet amount.
def get_bet():
    while True:
        bet_amount=input('Enter the bet amount for each line ('+ str(MIN_BET) +'-'+  str(MAX_BET)+') ')
        if bet_amount.isdigit():
            bet_amount=int(bet_amount)
            if MIN_BET<=bet_amount<=MAX_BET:
                return bet_amount
            else:
                print(f'Amount must be between {MIN_BET} - {MAX_BET}')
        else:
            print('Enter a valid bet amount.')

#Making of the slot machine.
def slot(rows,cols,symbols):
    tot_sym=[]
    for symbol,count in symbols.items():
        for _ in range(count):
            tot_sym.append(symbol)  

    columns=[]
    for col in range(cols):
        column=[]
        current_symbols=tot_sym[:]
        for row in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

#Rows need to be converted to columns and vice-versa.
def print_slot(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!= len(columns)-1:
                print(column[row],end=' | ')
            else:
                print(column[row],end='')
        print()

#Win amount calculation.
def Win(machine,lines,bet,value):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=machine[0][line]
        for column in machine:
            symbol_check=column[line]
            if symbol_check!=symbol:
                break
        else:
            winnings+=value[symbol]*bet
            winning_lines.append(line+1)
    return winnings,winning_lines

def spin(balance):
    lines=no_of_line()
    while True:
        bet=get_bet()
        total_bet = lines*bet 
        if total_bet > balance:
            print(f'Low Balance')
            break
        else:
            break
    print(f'Betting amount is {total_bet}.')
    
    slots=slot(ROWS,COLS,symbol_count)
    print_slot(slots)
    winning,winning_lines=Win(slots,lines,bet,symbol_value)
    print(f'you won {winning}')
    print(f'You won on lines:',*winning_lines)  
    return winning-total_bet

        


def main():
    balance=deposit()
    while True:
        print(f'Current balance is {balance}')
        ans=input('Press enter to spin/(q to quit)')
        if ans=='q':
            break
        else:
            if balance > 0:
                balance+=spin(balance)
                print(f'you left with {balance}')
            else:
                print('you donot have enough balance.')
                break
            
main()