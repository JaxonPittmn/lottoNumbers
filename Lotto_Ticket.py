import os, sys

file = open("tick_nums.txt", 'r')
tickSheet = file.read()

tickSheet = tickSheet.split("\n")

lottos=[]

ended = False

for ticket in tickSheet:
    ticket = ticket.split(" ")
    numt=[]
    for item in ticket:
        numt.append(int(item))
    lottos.append(numt)

while True:
    tim=0
    possible=[]
    ended=False
    print("New Ticket Set")

    while not ended and tim!=6:
        remove = []
        if tim!=0 and len(possible)==0:

            print("No Tickets")
            ended=True
            break

        tickn=int(input("Select> "))
        print("\n")

        if tim==0:
            for i,ticket in enumerate(lottos):
                if tickn in ticket:
              
                    possible.append(lottos[i])

        else:
            for i,ticket in enumerate(possible):
                if tickn not in ticket:
                    remove.append(ticket)

        for item in remove:
            possible.remove(item)

        if len(possible) != 0:
            print("Tickets left:")
            for ticket in possible:
                print(ticket)

        print("\n")
        tim += 1
        if tim==6:
            print(f"Winning Ticket: {possible[0]}")
            sys.exit()