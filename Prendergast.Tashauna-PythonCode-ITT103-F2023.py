# Author: Tashauna Prendergast
# Date Created: December 4, 2023
# Course: ITT103
# Purpose: Users must be able to make a reservation on the system, no duplication or invalid numbers are accepted.


# Define arrays

seat = []
prompt = ' '
available = True

first_class = 27
business_class = 30
economy_class = 56

seats_first = []
seats_business = []
seats_econ = []

# Menu options

menu = """ *** UCC Signature Express Limited ***
   *** Ride In Style And Comfort ***

Reservation Options:
First Class (F/f)
Business Class (B/b)
Economy Class (E/e)
Quit or Cancel (Q/q)

Please select an option:  """
print(" ")

# Start of  Outter While Statement

while not (prompt == 'q'):
    prompt = input(menu).lower()
    print(" ")

    if prompt == 'q':
        print(" ")
        print("*** Thank You For Booking With Us! ***")
        print(" ")
        print("- Reservation Type: First Class")
        print("- Total number of seats: ", first_class)
        print("- Total number of seats reserved: ", len(seats_first))
        print(" ")
        print("- Reservation Type: Business class")
        print("-Total number of seats: ", business_class)
        print("- Total number of seats reserved: ", len(seats_business))
        print(" ")
        print("- Reservation Type: Economy Class ")
        print("- Total number of seats: ", economy_class)
        print("- Total number of seats reserved: ", len(seats_econ))
        break
        print(" ")

    while not (prompt == 'f' or prompt == 'b' or prompt == 'e'):
        print("Invalid choice!")
        print(" ")

        
        prompt = input(menu)

# Define First Class Logic

    if prompt == 'f':
        if len(seats_first) < first_class:
            print("You Selected First Class")    
            print(" ")        
            print("Please enter your row number: 1 - 7 ")
            row_f = input()

        
            while not int(row_f) >= 1 and int(row_f) <= 7:
                print("Number must be positive or greater than zero! ")
                row_f = input("Enter a new row: ")
            print("Please select Window (W/w) or Aisle (A/a):")
            w_a = input().lower()
            print(" ")  

            if w_a == 'w':
                print("You selected window")
                col_f = 1

            if w_a == 'a':
                print("You selected aisle")
                col_f = 2
            seat_tmp = [row_f, col_f]
            available = 1
            
            for i in range(len(seats_first)):
              if (seat_tmp == seats_first[i]):
                  available = 0
                  break
              
            if(available == 1):            
                print("Reserving seat: row", row_f, " column", col_f)
                seats_first.append(seat_tmp)
                print(" ")

            else:
                print('Seat is already reserved')
                print("Please select a new option")
        else:
            print("No more available seats!")

# Define Business Class Logic

    elif prompt == 'b':
         if len(seats_business) < business_class:
            print("You Selected Business Class")
            print(" ")
            print("Please enter your row number: 1 - 10 ")
            row_b = input()

            while not int(row_b) >= 1 and int(row_b) <= 10:
                print(" Number must be positive or greater than zero! ")
                row_b = input("Enter a new row: ")
            print("Please select Window (W/w) or Aisle (A/a):")
            w_a2 = input().lower()
            print(" ")  

            if w_a2 == 'w':
                print("You selected window")
                col_b = 1

            if w_a2 == 'a':
                print("You selected aisle")
                col_b = 2
            seat_tmp2 = [row_b, col_b]
            available = 1
            
            for i in range(len(seats_business)):
              if (seat_tmp2 == seats_business[i]):
                  available = 0
                  break
            if(available == 1):
                print("Reserving seat: row", row_b, " column", col_b)
                seats_business.append(seat_tmp2)
                print(" ")

            else:
                print('Seat is already reserved')
                print("Please select a new option")
         else:
            print("No more available seats!")

# Define Economy Class Logic

    elif prompt =='e':
          if len(seats_econ) < economy_class:
            print("You Selected Economy Class")
            print(" ")
            print("Please enter your row number: 1 - 14 ")
            row_e = input()

            while not int(row_e) >= 1 and int(row_e) <= 14:
                print(" Number must be positive or greater than zero! ")
                row_e = input("Enter a new row: ")
            print("Please select Window (W/w) or Aisle (A/a):")
            w_a3 = input().lower()
            print(" ")  

            if w_a3 == 'w':
                print("You selected window")
                col_e = 1

            if w_a3 == 'a':
                print("You selected aisle")
                col_e = 2
            seat_tmp3 = [row_e, col_e]
            available = 1
            
            for i in range(len(seats_econ)):
              if (seat_tmp3 == seats_econ[i]):
                  available = 0
                  break
              
            if(available == 1):
                print("Reserving seat: row", row_e, " column", col_e)
                seats_econ.append(seat_tmp3)
                print(" ")

            else:
                print('Seat is already reserved')
                print("Please select a new option")
          else:
            print("No more available seats!")

