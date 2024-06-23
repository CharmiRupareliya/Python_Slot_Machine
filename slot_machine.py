import random
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)
# Initialize colorama to automatically reset colors after each print statement

# Constants for the slot machine game
MAX_LINES = 3
MAX_BET = 200
MIN_BET = 1

ROWS = 3   # Number of rows in the slot machine
COLS = 3   # Number of columns in the slot machine

# Dictionary to hold the count of each symbol
symbol_count = {
    "A": 2,     # 'A' symbol appears 2 times in the slot machine reel
    "B": 4,     # 'B' symbol appears 4 times in the slot machine reel
    "C": 6,     # 'C' symbol appears 6 times in the slot machine reel
    "D": 5      # 'D' symbol appears 8 times in the slot machine reel
}

symbol_value = {
    "A": 5,    # 'A' symbol multiplies the bet by 5 if it wins
    "B": 4,    # 'B' symbol multiplies the bet by 4 if it wins
    "C": 3,    # 'C' symbol multiplies the bet by 3 if it wins
    "D": 2     # 'D' symbol multiplies the bet by 2 if it wins
}
print(Fore.CYAN + Style.BRIGHT + "Welcome to Slot Machine Game...")
print()

# Function to check winnings based on the slot machine outcome
def check_winnigs(columns, lines, bet, values):
    winnings = 0          # Total winnings from the spin
    winning_lines = []     # List to store the winning line numbers

    # Loop through each line to check for winnings
    for line in range(lines):
        symbol = columns[0][line]  # Get the symbol on the current line from the first column
        for column in columns:
            symbol_to_check = column[line]  # Check the symbol on the current line from each column
            if symbol != symbol_to_check:
                break     # If any symbol doesn't match, stop checking further
        else:
            winnings += values[symbol] * bet   # If all symbols in the line match, add the winnings for that line
            winning_lines.append(line + 1)    # Add the line number to the winning lines list

    return winnings, winning_lines

# Function to spin the slot machine and generate the columns with symbols
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []

    # Create a list of all symbols based on their counts
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []

    # Generate each column by randomly selecting symbols
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)  # Randomly select a symbol for the column
            current_symbols.remove(value)      # Remove the selected symbol to avoid repetition in the same column
            column.append(value)

        columns.append(column)

    return columns

# Function to print the slot machine columns
def print_slot_machine(columns):

    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end= " | ")
            else:
                print(column[row])

    return

# Function to get the deposit amount from the player
def deposit():
    while True:
        amount = input(Fore.BLACK + Style.BRIGHT + "What would you like to deposit? Rs.")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break
            else:
                print(Fore.RED + "Amount must be greater than zero.")

        else:
            print(Fore.RED + "Please enter a number.")
    return amount

# Function to get the number of lines to bet on from the player
def get_number_of_lines():
    while True:
        lines = input(Fore.BLACK + Style.BRIGHT + "Enter the number of lines to bet on(1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(Fore.RED + "Enter a valid number of lines.")
        else:
            print(Fore.RED + "Please Enter a number.")
    return lines

# Function to get the bet amount per line from the player
def get_bet():
    while True:
        amount = input(Fore.BLACK + Style.BRIGHT + "What would you like to bet on each line? Rs.")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(Fore.RED + f"Amount must be between Rs.{MIN_BET} - Rs.{MAX_BET}")
        else:
            print(Fore.RED + "Please Enter a number.")
    return amount

# Function to handle a spin of the slot machine
def spin(balance=None):
    lines = get_number_of_lines()  # Get the number of lines to bet on

    while True:
        bet = get_bet()    # Get the bet amount per line
        total_bet = bet * lines  # Calculate the total bet

        if total_bet > balance:
            print(Fore.RED + f"You do not have enough to bet that amount, Your current balance is: Rs.{balance}")
        else:
            break

    print(f"You are betting Rs.{bet} on {lines} lines. Total bet is equal to : Rs.{total_bet} ")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)  # Spin the slot machine to get columns with symbols
    print_slot_machine(slots)    # Print the slot machine outcome
    winnings, winning_lines = check_winnigs(slots, lines, bet, symbol_value)    # Check the winnings based on the outcome
    print(f"You won Rs.{winnings}")
    print("You won on lines:", *winning_lines)

    return winnings - total_bet  # Return the net result of the spin (winnings - total bet)

# Main function to run the slot machine game
def main():
    balance = deposit()   # Get the initial deposit from the player
    while True:
        print(Fore.MAGENTA + f"Current balance is Rs.{balance}")
        ans = input(Fore.BLUE + "Press enter to play (q to quit).")
        print()
        if ans == "q":
            break
        balance +=  spin(balance)    # Update the balance based on the result of the spin
    print(f"You left with Rs.{balance}")
    print(Fore.CYAN + Style.BRIGHT + "Thank you for Playing...")

main()  # Run the main function to start the game
