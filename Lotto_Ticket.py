import os, sys

# Open the file containing ticket numbers for reading
file = open("tick_nums.txt", 'r')
tickSheet = file.read()

# Split the file content into lines, each representing a ticket
tickSheet = tickSheet.split("\n")

lottos=[]

ended = False

# Parse each ticket line into a list of integers and add to lottos
for ticket in tickSheet:
    ticket = ticket.split(" ")
    numt=[]
    for item in ticket:
        numt.append(int(item))
    lottos.append(numt)

while True:
    """
    Main loop for processing ticket selection.
    Allows the user to iteratively filter tickets based on input numbers.
    """
    tim=0
    possible=[]
    ended=False
    print("New Ticket Set")

    while not ended and tim!=6:
        remove = []
        # If not the first round and no possible tickets remain, end the loop
        if tim!=0 and len(possible)==0:
            print("No Tickets")
            ended=True
            break

        # Prompt user to select a number
        tickn=int(input("Select> "))
        print("\n")

        if tim==0:
            # On the first round, filter all tickets containing the selected number
            for i,ticket in enumerate(lottos):
                if tickn in ticket:
                    possible.append(lottos[i])
        else:
            # On subsequent rounds, remove tickets that do not contain the selected number
            for i,ticket in enumerate(possible):
                if tickn not in ticket:
                    remove.append(ticket)

        # Remove tickets that do not match the current selection
        for item in remove:
            possible.remove(item)

        # Display remaining possible tickets
        if len(possible) != 0:
            print("Tickets left:")
            for ticket in possible:
                print(ticket)

        print("\n")
        tim += 1
        # If 6 numbers have been selected, print the winning ticket and exit
        if tim==6:
            print(f"Winning Ticket: {possible[0]}")
            sys.exit()