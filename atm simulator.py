#!/usr/bin/env python3

pin = 123456
balance = 1000.00

def ask_to_exit():
    try:
        print("(1) Yes | (2) No")
        abcde = int(input("Would you like to continue the transaction? Please enter a digit either 1 or 2 to continue."))
        if abcde == 1:
            return True
        elif abcde == 2:
            print("Thank you for using this ATM.")
            exit()
        else:
            print("Sorry , this was an invalid response . Please try again.")
            return 
    except ValueError:
        print("Sorry , this was an invalid response . Please try again.")
        return 

def pin_page():
    try:
        typing = int(input("Hello , please enter your PIN."))
        if typing == pin:
            return True
        elif typing != pin:
            print("Sorry , please try again.")
            return False
    except ValueError:
        print("Sorry , please try again.")
        return False

attempts = 0 
while attempts < 3:
    success = pin_page()
    if success:
        break  
    else:
        attempts = attempts + 1
        remaining = 3 - attempts
        if remaining > 0:
            print(f"You have {remaining} attempts remaining.")
        else:
            print("TOO MANY INCORRECT ATTEMPTS. ACCOUNT LOCKED.")
            exit() 

def atm_menu():
    try:
        global balance
        global pin
        print("Please select a transaction to continue.")
        print("(1) --- Withdrawal")
        print("(2) --- Balance Inquiry") 
        print("(3) --- Change your pin number")
        print("(4) --- Factory reset (SPECIAL FOR THIS ATM SIMULATOR ONLY)")
        print("(5) --- Deposit")
        print("(6) --- Return card")
        selection = int(input("Please enter a digit either 1 , 2 , 3 , 4 , 5 or 6 to continue."))
        if selection == 1:
            print("Please select an amount to continue.")
            print("(1) RM100 | (2) RM400 | (3) RM800 | (4) RM1100")
            print("(5) RM1400 | (6) RM1700 | (7) Other amount | (8) Main menu")
            one_input = int(input("Please enter a digit either 1 , 2 , 3 , 4 , 5 , 6 , 7 or 8 to continue."))
            amounts = {1: 100, 2: 400, 3: 800, 4: 1100, 5: 1400, 6: 1700}
            if one_input in amounts:
                cash = amounts[one_input] 
                if cash <= balance:
                    balance = round(balance - cash, 2)
                    print(f"Transaction successful! Your current balance is RM{balance:.2f} ")
                    ask_to_exit()
                else:
                    print(f"Insufficient funds! You only have RM{balance:.2f}.")
            elif one_input == 7:
                oa = float(input("Please enter your desired amount: "))
                if 0 < oa <= balance and round(oa * 100) % 5 == 0:
                    balance = round(balance - oa, 2)
                    print(f"Transaction successful! Your current balance is RM{balance:.2f}")
                    ask_to_exit()
                else:
                    print("Invalid amount. You cannot withdraw RM0 , negative amount , unrealistic amounts , amounts exceeding your balance or with excessive decimals.")
                    return 
            elif one_input == 8:
                return 
            else:
                print("Invalid response.")
                return  
        elif selection == 2:
            print(f"Your balance is RM{balance:.2f}")
            ask_to_exit()
        elif selection == 3:
            original_pin = int(input("Enter your original PIN  . If you wish to return to the main menu , enter any number or letter once and you will be returned to the menu. "))
            if original_pin == pin:
                new_pin_input = input("Please enter your desired new PIN (4-6 digits).: ")
                if new_pin_input.isdigit() and 4 <= len(new_pin_input) <= 6:
                    new_pin = int(new_pin_input)
                    confirm_pin = int(input("Please reenter your desired new PIN for verification."))
                    if new_pin == confirm_pin:
                        pin = new_pin
                        print("Your PIN has been changed successfully.")
                        ask_to_exit()
                    else:
                        print("Sorry , the verification of the new pin number failed , the pin number will not be changed . Please try again.")
                        return
                else:
                    print("The number of digits was not sufficient . Please try again.") 
            else:
                print("Incorrect pin number.")
                return 
        elif selection == 4:
            balance = 1000.00
            pin = 123456
            print("System fully reset.")
            print("(1) Yes | (2) No")
            fffff = int(input("Would you like to try the simulator again? Please enter a digit either 1 or 2 to continue."))
            if fffff == 1:
                return
            else:
                print("Thank you for using this ATM.")
                exit()
        elif selection == 5:
            akaun = int(input("Please enter your account number , If you wish to return to the main menu , enter any number or letter once and you will be returned to the menu.:"))
            nas = 1234567890
            if akaun == nas:
                print("Account number verified.")
            else:
                print("Wrong account number.")
                return

            running_total = 0.0
            while True:
                dep = float(input("Enter the amount you would like to deposit."))
                if dep > 0 and round(dep * 100) % 5 == 0:
                    running_total = round(running_total + dep, 2)
                    print(f"Your intended deposit amount is : RM{running_total:.2f} . Would you like to proceed?")
                    print("(1) Add amount | (2) Yes | (3) No")
                    option = int(input("Please enter a digit either 1 , 2 or 3 to continue."))
                    if option == 1:
                        continue
                    elif option == 2:
                        balance = round(balance + running_total, 2)
                        print(f"Transaction successful! RM{running_total:.2f} has been deposited into your account.")
                        print(f"New balance: RM{balance:.2f}")
                        ask_to_exit()
                        return
                    elif option == 3:
                        print(f"Your deposited amount of RM{running_total:.2f} has been returned.")
                        return
                else:
                    print("Invalid amount. You cannot deposit RM0 , negative amounts , unrealistic amounts or amounts that contains excessive decimals.")
                    return
                    
        elif selection == 6:
            print("Thank you for using this ATM.")
            exit()
    except ValueError:
        print("Sorry , this was an invalid response . Please try again.")
        return 
while True:
    atm_menu()







        
            
    
