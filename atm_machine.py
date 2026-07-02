account_holder_name = "Akshay Chauhan"
pin = 1234
balance = 10000
wrong_attempt = 0

while wrong_attempt < 3:
    entered_pin = int(input("enter you pin: "))

    if entered_pin == pin:
        print("correct pin")

        while True:
            print("\n****Welcome To ATM Machine")
            print("1. account holder name")
            print("2. balance")
            print("3. deposit")
            print("4. withdraw")
            print("5. change pin")
            print("6. exit")

            choice = input("enter your choice: ")

            if choice == "1":

                print("account holder name is: ",account_holder_name)
                
            elif choice == "2":

                print("your balance: ",balance)

            elif choice == "3":

                amount = int(input("enter your deposit amount: "))

                if amount > 0:
                    balance+=amount

                    print("amount deposit successfully")
                    print("new balance: ",balance)

                else:
                    print("deposit amount should be greater than 0")

            elif choice == "4":

                amount = int(input("enter your withdraw amount: "))

                if amount <= 0:

                    print("withdraw amount should be greater than 0")

                elif amount <= balance:
                    balance-=amount

                    print("amount withdraw successfully")
                    print("new balance: ",balance)

                else:
                    print("insufficient balance")

            elif choice == "5":
                old_pin_attempt = 0

                while old_pin_attempt < 3:
                    old_pin = int(input("enter old pin: "))

                    if old_pin == pin:
                        new_pin = int(input("enter new pin:"))

                        if new_pin >= 1000 and new_pin <=9999:
                            confirm_pin = int(input("enter confirm pin: "))

                            if confirm_pin == new_pin:
                                pin = new_pin
                                print("pin change successfully")
                                break

                            else:
                                print("confirm pin is wrong")
                                break

                        else:
                            print("pin should be exactly 4 digits")
                            break

                    else:
                     old_pin_attempt += 1
                     print("old pin is wrong")
                     print("attempts left: ", 3 - old_pin_attempt)

                if old_pin_attempt == 3:
                    print("your account has been blocked due to 3 wrong old PIN attempts")
                    break

            elif choice == "6":
                print("Thnak You")
                break
            
            else:
                print("invalid choice")

        break

    else:
        wrong_attempt += 1
        print("wrong pin")
        print("attempts left: ", 3 - wrong_attempt)

if wrong_attempt == 3:
    print("\nyour account has been blocked due to 3 wrong PIN attempts")
