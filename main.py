# The program starts with the main function and takes into consideration code optimization.
# A dictionary was created to generate a numbering system for the different types of rooms.
# It also keeps track of the state of the room, i.e, if its available and checked in or not
# Dictionary key:
# 1 => Yes
# 0 => No
# 2 => Part Payment **For only the Fully Paid attribute
#

EXECUTIVE_AMOUNT = 2500
EXECUTIVE_AMOUNT_DISABLED = 2500 - (0.1 * 2500)
CHALET_AMOUNT = 1500
CHALET_AMOUNT_DISABLED = 1500 - (0.1 * 1500)
ORDINARY_AMOUNT = 500
ORDINARY_AMOUNT_DISABLED = 500 - (0.1 * 500)
available_room_list = []
customer_name = ''
customer_tel = 0
room_name = ''
room_type = '' #Indicates the category of room wanted by the user, i.e 1 = Executive, 2 = Chalet, 3 = Ordinary

executive_rooms = {
    'E-01': {
        'Availability': 1,
        'Checked-In': 0,
        'Fully Paid': 0,
        'Disability': 0,
        'Number of Nights': 0
    },
    'E-02': {
        'Availability': 1,
        'Checked-In': 0,
        'Fully Paid': 0,
        'Disability': 1,
        'Number of Nights': 0
    },
    'E-03': {
        'Availability': 1,
        'Checked-In': 0,
        'Fully Paid': 0,
        'Disability': 1,
        'Number of Nights': 0
    },
    'E-04': {
        'Availability': 1,
        'Checked-In': 0,
        'Fully Paid': 0,
        'Disability': 0,
        'Number of Nights': 0
    },
    'E-05': {
        'Availability': 1,
        'Checked-In': 0,
        'Fully Paid': 0,
        'Disability': 0,
        'Number of Nights': 0
    },
    'E-06': {
        'Availability': 1,
        'Checked-In': 0,
        'Fully Paid': 0,
        'Disability': 0,
        'Number of Nights': 0
    },
    'E-07': {
        'Availability': 1,
        'Checked-In': 0,
        'Fully Paid': 0,
        'Disability': 0,
        'Number of Nights': 0
    },
    'E-08': {
        'Availability': 1,
        'Checked-In': 0,
        'Fully Paid': 0,
        'Disability': 0,
        'Number of Nights': 0
    },
    'E-09': {
        'Availability': 1,
        'Checked-In': 0,
        'Fully Paid': 0,
        'Disability': 0,
        'Number of Nights': 0
    },
    'E-10': {
        'Availability': 1,
        'Checked-In': 0,
        'Fully Paid': 0,
        'Disability': 0,
        'Number of Nights': 0
    },
}

chalet_rooms = {
    'C-01': {
        'Availability': 1,
        'Checked-In': 0,
        'Fully Paid': 0,
        'Disability': 0,
        'Number of Nights': 0
    },
    'C-02': {
        'Availability': 1,
        'Checked-In': 0,
        'Fully Paid': 0,
        'Disability': 0,
        'Number of Nights': 0
    },
    'C-03': {
        'Availability': 1,
        'Checked-In': 0,
        'Fully Paid': 0,
        'Disability': 0,
        'Number of Nights': 0
    },
    'C-04': {
        'Availability': 1,
        'Checked-In': 0,
        'Fully Paid': 0,
        'Disability': 0,
        'Number of Nights': 0
    },
    'C-05': {
        'Availability': 1,
        'Checked-In': 0,
        'Fully Paid': 0,
        'Disability': 1,
        'Number of Nights': 0
    },
    'C-06': {
        'Availability': 1,
        'Checked-In': 0,
        'Fully Paid': 0,
        'Disability': 0,
        'Number of Nights': 0
    },
    'C-07': {
        'Availability': 1,
        'Checked-In': 0,
        'Fully Paid': 0,
        'Disability': 1,
        'Number of Nights': 0
    }
}
ordinary_rooms = {
    'O-01': {
        'Availability': 1,
        'Checked-In': 0,
        'Fully Paid': 0,
        'Disability': 1,
        'Number of Nights': 0
    },
    'O-02': {
        'Availability': 1,
        'Checked-In': 0,
        'Fully Paid': 0,
        'Disability': 0,
        'Number of Nights': 0
    },
    'O-03': {
        'Availability': 1,
        'Checked-In': 0,
        'Fully Paid': 0,
        'Disability': 0,
        'Number of Nights': 0
    },
    'O-04': {
        'Availability': 1,
        'Checked-In': 0,
        'Fully Paid': 0,
        'Disability': 0,
        'Number of Nights': 0
    },
    'O-05': {
        'Availability': 1,
        'Checked-In': 0,
        'Fully Paid': 0,
        'Disability': 1,
        'Number of Nights': 0
    },
    'O-06': {
        'Availability': 1,
        'Checked-In': 0,
        'Fully Paid': 0,
        'Disability': 0,
        'Number of Nights': 0
    },
    'O-07': {
        'Availability': 1,
        'Checked-In': 0,
        'Fully Paid': 0,
        'Disability': 1,
        'Number of Nights': 0
    }
}

#Starting function of the program
def main():
    start = int(input('\n\nHello Adventurer! Nice to Meet You.\nHow may I help you?\n'
                      '1. Book A Room\n2. Check Out \n3. Check Room Details\n4. Exit\n=> '))
    if start == 1:
        amount_to_pay = bookRoom()
        print('\nAmount Due: Ghc ' + str(amount_to_pay))
        balance = payAmount(amount_to_pay)
        step = int(input('\n\nPayment has been paid successfully. Here is your balance: Ghc ' + str(
            balance) + '\n1. Check In\n2. Print Receipt\n3. Go to Main Menu\n=> '))
        if step == 1:
            checkIn()
            step = int(input('\nYou are now checked into Room ' + room_name + '\n1. Check out of Room \n2.Go to Main Menu\n=> '))
            if step == 1:
                checkOut(room_name)
            elif step == 2:
                available_room_list.clear()
                main()
        elif step == 2:
            printReceipt(amount_to_pay)
            step = int(input('1. Go to Main Menu\n=> '))
            if step == 1:
                available_room_list.clear()
                main()
        elif step == 3:
            available_room_list.clear()
            main()
    elif start == 2:
        step = input('\nEnter Room Number to check out from\n=> ')
        checkOut(step)
    elif start == 3:
        checkForRoomDetails()
    elif start == 4:
        print("Thank you for patronizing our services. Please come back later.")
        exit()
    else:
        print('Something went wrong. Please try again later.')
        available_room_list.clear()
        main()


#Returns a formatted string of the transaction of the customer
#Required argument is the amount paid by customer
def printReceipt(amount_paid):
    receipt = '===============================================\n\t\tHOTEL DELUXE\n===============================================\n' \
              'Name of Customer: ' + customer_name + '\n' \
                                                     'Telephone Number: ' + str(customer_tel) + '\n' \
                                                                                                'Room Booked: ' + room_name + '\n'
    if room_type == 1:
        receipt += 'Category of Room: Executive\n'
        if executive_rooms[room_name]['Disability'] == 1:
            receipt += 'Disability Friendly: Yes\n'
        else:
            receipt += 'Disability Friendly: No\n'
    elif room_type == 2:
        receipt += 'Category of Room: Chalet\n'
        if chalet_rooms[room_name]['Disability'] == 1:
            receipt += 'Disability Friendly: Yes\n'
        else:
            receipt += 'Disability Friendly: No\n'
    elif room_type == 3:
        receipt += 'Category of Room: Ordinary\n'
        if ordinary_rooms[room_name]['Disability'] == 1:
            receipt += 'Disability Friendly: Yes\n'
        else:
            receipt += 'Disability Friendly: No\n'

    receipt += 'Amount Paid: Ghc ' + str(amount_paid)
    print(receipt)


#Returns the amount due to be paid, after the customer has requested a room
#Required argument is the number of nights the customer want the room for
def getAmountDue(nights_num):
    if room_type == 1:
        if executive_rooms[room_name]['Disability'] == 1:
            return nights_num * EXECUTIVE_AMOUNT_DISABLED
        else:
            return nights_num * EXECUTIVE_AMOUNT
    elif room_type == 2:
        if chalet_rooms[room_name]['Disability'] == 1:
            return nights_num * CHALET_AMOUNT_DISABLED
        else:
            return nights_num * CHALET_AMOUNT
    elif room_type == 3:
        if ordinary_rooms[room_name]['Disability'] == 1:
            return nights_num * ORDINARY_AMOUNT_DISABLED
        else:
            return nights_num * ORDINARY_AMOUNT

#Returns the name of the room
#Required argument is the index value of the room selected by the customer in available_room_list
def getRoomName(num):
    return available_room_list[num]

#Returns a formatted string of the details of a chosen room
def getRoomDetails():
    room_str = 'Room ' + room_name + ' Details\n'
    if room_type == 1:
        if executive_rooms[room_name]['Availability'] == 1:
            room_str += 'Availability: Yes\n'
        else:
            room_str += 'Availability: No\n'
            if executive_rooms[room_name]['Checked-In'] == 1:
                room_str += 'Checked-In Status: Yes\n'
            else:
                room_str += 'Checked-In Status: Not Yet\n'

            if executive_rooms[room_name]['Fully Paid'] == 1:
                room_str += 'Payment: Paid in Full\n'
            else:
                room_str += 'Payment: Part Payment\n'
        if executive_rooms[room_name]['Disability'] == 1:
            room_str += 'Disability Friendly: Yes\n'
            room_str += 'Amount Per Night: Ghc ' + str(EXECUTIVE_AMOUNT_DISABLED) + '\n'
        else:
            room_str += 'Disability Friendly: No\n'
            room_str += 'Amount Per Night: Ghc ' + str(EXECUTIVE_AMOUNT) + '\n'
    elif room_type == 2:
        if chalet_rooms[room_name]['Availability'] == 1:
            room_str += 'Availability: Yes\n'
        else:
            room_str += 'Availability: No\n'
            if chalet_rooms[room_name]['Checked-In'] == 1:
                room_str += 'Checked-In Status: Yes\n'
            else:
                room_str += 'Checked-In Status: Not Yet\n'

            if chalet_rooms[room_name]['Fully Paid'] == 1:
                room_str += 'Payment: Paid in Full\n'
            else:
                room_str += 'Payment: Part Payment\n'
        if chalet_rooms[room_name]['Disability'] == 1:
            room_str += 'Disability Friendly: Yes\n'
            room_str += 'Amount Per Night: Ghc ' + str(CHALET_AMOUNT_DISABLED) + '\n'
        else:
            room_str += 'Disability Friendly: No\n'
            room_str += 'Amount Per Night: Ghc ' + str(CHALET_AMOUNT) + '\n'
    elif room_type == 3:
        if ordinary_rooms[room_name]['Availability'] == 1:
            room_str += 'Availability: Yes\n'
        else:
            room_str += 'Availability: No\n'
            if ordinary_rooms[room_name]['Checked-In'] == 1:
                room_str += 'Checked-In Status: Yes\n'
            else:
                room_str += 'Checked-In Status: Not Yet\n'

            if ordinary_rooms[room_name]['Fully Paid'] == 1:
                room_str += 'Payment: Paid in Full\n'
            else:
                room_str += 'Payment: Part Payment\n'
        if ordinary_rooms[room_name]['Disability'] == 1:
            room_str += 'Disability Friendly: Yes\n'
            room_str += 'Amount Per Night: Ghc ' + str(ORDINARY_AMOUNT_DISABLED) + '\n'
        else:
            room_str += 'Disability Friendly: No\n'
            room_str += 'Amount Per Night: Ghc ' + str(ORDINARY_AMOUNT) + '\n'

    return room_str

#Asks for customer's name and telephone number
def register_customer():
    global customer_name
    global customer_tel
    customer_name = input('Enter First Name: ')
    customer_tel = int(input('Enter Telephone Number: '))

#Takes the customer through the process of booking a room
def bookRoom():
    global room_name
    global room_type
    step = int(input('\n\nWe have 24 rooms and three category of rooms. Which category of room are you interested in?\n'
                     '1. Executive\n2. Chalet\n3. Ordinary\n=> '))
    room_type = step
    room_num = int(input('\n\nWe have ' + str(
        getAvailableRooms()) + ' rooms available. Please pick a room of your choice\n' + getAvailableRoomsList() + '\n=> '))

    # 1 is subtracted from room_num to get the index of the room chosen by the customer in the list available_room_list
    room_num -= 1
    room_name = getRoomName(room_num)
    step = int(input('\n\n' + getRoomDetails() + '1. Book Room\n=> '))
    amount_pay = 0
    if step == 1:
        print('\n\nRoom ' + room_name + ' Booking Sheet\n')
        register_customer()
        nights_num = int(input('How many nights do you want the room for? \n=> '))
        amount_pay = getAmountDue(nights_num)
        if room_type == 1:
            executive_rooms[room_name]['Number of Nights'] = nights_num
        elif room_type == 2:
            chalet_rooms[room_name]['Number of Nights'] = nights_num
        elif room_type == 3:
            ordinary_rooms[room_name]['Number of Nights'] = nights_num
    return amount_pay

#Checks out a room by resetting all its attributes to its default
#Required argument is the string name of the room
def checkOut(room):
    room_char = room[:1]
    if room_char == 'E':
        if executive_rooms[room]['Checked-In'] == 1:
            executive_rooms[room]['Checked-In'] = 0
            executive_rooms[room]['Availability'] = 1
            executive_rooms[room]['Fully Paid'] = 0
            executive_rooms[room]['Number of Nights'] = 0
            step = int(input('You have successfully checked out of Room ' + room +'\n1. Main Menu\n=> '))
            if step == 1:
                available_room_list.clear()
                main()
        else:
            step = int(input('Sorry. You are not checked into this room\n1. Main Menu\n=> '))
            if step == 1:
                available_room_list.clear()
                main()
    elif room_char == 'C':
        if chalet_rooms[room]['Checked-In'] == 1:
            chalet_rooms[room]['Checked-In'] = 0
            chalet_rooms[room]['Availability'] = 1
            chalet_rooms[room]['Fully Paid'] = 0
            chalet_rooms[room]['Number of Nights'] = 0
            step = int(input('You have successfully checked out of Room ' + room + '\n1. Main Menu\n=> '))
            if step == 1:
                available_room_list.clear()
                main()
        else:
            step = int(input('Sorry. You are not checked into this room\n1. Main Menu\n=> '))
            if step == 1:
                available_room_list.clear()
                main()
    elif room_char == 'O':
        if ordinary_rooms[room]['Checked-In'] == 1:
            ordinary_rooms[room]['Checked-In'] = 0
            ordinary_rooms[room]['Availability'] = 1
            ordinary_rooms[room]['Fully Paid'] = 0
            ordinary_rooms[room]['Number of Nights'] = 0
            step = int(input('You have successfully checked out of Room ' + room + '\n1. Main Menu\n=> '))
            if step == 1:
                available_room_list.clear()
                main()
        else:
            step = int(input('Sorry. You are not checked into this room\n1. Main Menu\n=> '))
            if step == 1:
                available_room_list.clear()
                main()
    else:
        print('Error! Wrong Input Value')
        available_room_list.clear()
        main()

#Checks the customer in
def checkIn():
    if room_type == 1:
        executive_rooms[room_name]['Checked-In'] = 1
        executive_rooms[room_name]['Availability'] = 0
    elif room_type == 2:
        chalet_rooms[room_name]['Checked-In'] = 1
        chalet_rooms[room_name]['Availability'] = 0
    elif room_type == 3:
        ordinary_rooms[room_name]['Checked-In'] = 1
        ordinary_rooms[room_name]['Availability'] = 0

#Returns the number of available rooms for a particular room type
def getAvailableRooms():
    room_num = 0
    if room_type == 1:
        for room, room_info in executive_rooms.items():
            room_num += room_info['Availability']
    elif room_type == 2:
        for room, room_info in chalet_rooms.items():
            room_num += room_info['Availability']
    elif room_type == 3:
        for room, room_info in ordinary_rooms.items():
            room_num += room_info['Availability']
    return room_num

#Returns a formatted string of the available list of rooms of a particular room type
def getAvailableRoomsList():
    room_str = ''
    if room_type == 1:
        for room, room_info in executive_rooms.items():
            if room_info['Availability'] == 1:
                available_room_list.append(room)
    elif room_type == 2:
        for room, room_info in chalet_rooms.items():
            if room_info['Availability'] == 1:
                available_room_list.append(room)
    elif room_type == 3:
        for room, room_info in ordinary_rooms.items():
            if room_info['Availability'] == 1:
                available_room_list.append(room)

    count = 1
    for item in available_room_list:
        room_str += str(count) + '. ' + item + '\n'
        count += 1

    return room_str

#Processes the amount inputted by the user and returns the balance
def payAmount(amount_to_pay):
    amount = int(input('Enter Payment: '))
    if amount == amount_to_pay:
        if room_type == 1:
            executive_rooms[room_name]['Fully Paid'] = 1
        elif room_type == 2:
            chalet_rooms[room_name]['Fully Paid'] = 1
        elif room_type == 3:
            ordinary_rooms[room_name]['Fully Paid'] = 1
        return 0.00
    elif amount < amount_to_pay:
        arrears = amount_to_pay - amount
        if room_type == 1:
            executive_rooms[room_name]['Fully Paid'] = 2
        elif room_type == 2:
            chalet_rooms[room_name]['Fully Paid'] = 2
        elif room_type == 3:
            ordinary_rooms[room_name]['Fully Paid'] = 2
        step = int(input('\n\nArrears: Ghc ' + str(
            arrears) + '\nYou must pay all the amount in order to be able to check-in\n1. Pay Arrears\n2. Go to Main Menu\n=> '))
        if step == 1:
            payAmount(arrears)
        elif step == 2:
            available_room_list.clear()
            main()
    else:
        balance = amount - amount_to_pay
        if room_type == 1:
            executive_rooms[room_name]['Fully Paid'] = 1
        elif room_type == 2:
            chalet_rooms[room_name]['Fully Paid'] = 1
        elif room_type == 3:
            ordinary_rooms[room_name]['Fully Paid'] = 1
        return balance

#Checks for details of room
def checkForRoomDetails():
    global room_type
    step = input('Search For Details of Room Here\nEnter Room Number: ')
    room = step
    room_char = room[:1]
    room_str = '\nRoom ' + room + ' Details\n'
    if room_char == 'E':
        if executive_rooms[room]['Availability'] == 1:
            room_str += 'Availability: Yes\n'
        else:
            room_str += 'Availability: No\n'
            if executive_rooms[room]['Checked-In'] == 1:
                room_str += 'Checked-In Status: Yes\n'
            else:
                room_str += 'Checked-In Status: Not Yet\n'

            if executive_rooms[room]['Fully Paid'] == 1:
                room_str += 'Payment: Paid in Full for ' + str(executive_rooms[room]['Number of Nights']) + ' Nights\n'
            else:
                room_str += 'Payment: Part Payment for ' + str(executive_rooms[room]['Number of Nights']) + ' Nights\n'
        if executive_rooms[room]['Disability'] == 1:
            room_str += 'Disability Friendly: Yes\n'
            room_str += 'Amount Per Night: Ghc ' + str(EXECUTIVE_AMOUNT_DISABLED) + '\n'
        else:
            room_str += 'Disability Friendly: No\n'
            room_str += 'Amount Per Night: Ghc ' + str(EXECUTIVE_AMOUNT) + '\n'
    elif room_char == 'C':
        if chalet_rooms[room]['Availability'] == 1:
            room_str += 'Availability: Yes\n'
        else:
            room_str += 'Availability: No\n'
            if chalet_rooms[room]['Checked-In'] == 1:
                room_str += 'Checked-In Status: Yes\n'
            else:
                room_str += 'Checked-In Status: Not Yet\n'

            if chalet_rooms[room]['Fully Paid'] == 1:
                room_str += 'Payment: Paid in Full for ' + str(chalet_rooms[room]['Number of Nights']) + ' Nights\n'
            else:
                room_str += 'Payment: Part Payment for ' + str(chalet_rooms[room]['Number of Nights']) + ' Nights\n'
        if chalet_rooms[room]['Disability'] == 1:
            room_str += 'Disability Friendly: Yes\n'
            room_str += 'Amount Per Night: Ghc ' + str(CHALET_AMOUNT_DISABLED) + '\n'
        else:
            room_str += 'Disability Friendly: No\n'
            room_str += 'Amount Per Night: Ghc ' + str(CHALET_AMOUNT) + '\n'
    elif room_char == 'O':
        if ordinary_rooms[room]['Availability'] == 1:
            room_str += 'Availability: Yes\n'
        else:
            room_str += 'Availability: No\n'
            if ordinary_rooms[room]['Checked-In'] == 1:
                room_str += 'Checked-In Status: Yes\n'
            else:
                room_str += 'Checked-In Status: Not Yet\n'

            if ordinary_rooms[room]['Fully Paid'] == 1:
                room_str += 'Payment: Paid in Full for ' + str(ordinary_rooms[room]['Number of Nights']) + ' Nights\n'
            else:
                room_str += 'Payment: Part Payment for ' + str(ordinary_rooms[room]['Number of Nights']) + ' Nights\n'
        if ordinary_rooms[room]['Disability'] == 1:
            room_str += 'Disability Friendly: Yes\n'
            room_str += 'Amount Per Night: Ghc ' + str(ORDINARY_AMOUNT_DISABLED) + '\n'
        else:
            room_str += 'Disability Friendly: No\n'
            room_str += 'Amount Per Night: Ghc ' + str(ORDINARY_AMOUNT) + '\n'
    print(room_str)
    step = int(input('\n1. Search Again\n2. Go to Main Menu\n=> '))
    if step == 1:
        checkForRoomDetails()
    elif step == 2:
        available_room_list.clear()
        main()


# Main Program Thread
main()