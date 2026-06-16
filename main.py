import random

MAX_LINES = 3
MAX_BET = 500
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 5,
    "D": 6,
    "E": 6,
    "F": 20,
}

symbol_values = {
    "A": 10,
    "B": 5,
    "C": 4,
    "D": 3,
    "E": 1,
    "F": 0,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else: 
            winnings += values[symbol] * bet
    return winnings
            
            

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #copy array
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="|")
            else: 
                print(column[row])

def deposit():
    while True:
        amount = input("Amount to Deposit: P")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be more than 0")
                
        else: 
            print("Please enter a number")

    return amount

def get_number_of_lines():
    while True: 
        lines = input("Please enter amount of Lines to bet: (1 - " + str(MAX_LINES) + ")?: ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a Valid of Lines")
        else: 
            print("Please enter a number")
    
    return lines

def get_bet():
    while True:
        bet = input("Amount to Bet: P")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be more {MIN_BET} - {MAX_BET}")
        else: 
            print("Please enter a number")

    return bet

def get_valid_bet(balance, lines):
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"Insufficient Balance: Balance {balance}")
            print(f"The Total bet is {total_bet}")
        else:
            return bet, total_bet

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet, total_bet = get_valid_bet(balance, lines) 
    
    print("---")
    print(f"Balance: P{balance}")
    print(f"Lines playing: {lines}")
    print(f"Bet per line: P{bet}")
    print(f"Total Bet: P{total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots) 
    
    winnings = check_winnings(slots, lines, bet, symbol_values)
    print(f"You Won P{winnings}")



main()  
        