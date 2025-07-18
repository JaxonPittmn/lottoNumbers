import os
import sys

def main():
    """
    Main entry point for the lottery ticket filtering script.

    Reads ticket numbers from 'tick_nums.txt', then allows the user to iteratively
    filter tickets by entering numbers. After each number, only tickets containing
    all selected numbers remain. When 6 numbers are selected, the script displays
    the matching ticket and exits.
    """
    # Open the file containing ticket numbers for reading
    with open("tick_nums.txt", 'r') as file:
        tickSheet = file.read()

    # Split the file content into lines, each representing a ticket
    tickSheet = tickSheet.strip().split("\n")

    lottos = []

    # Parse each ticket line into a list of integers and add to lottos
    for ticket in tickSheet:
        ticket = ticket.strip().split(" ")
        numt = []
        for item in ticket:
            numt.append(int(item))
        lottos.append(numt)

    while True:
        """
        Main loop for processing ticket selection.

        Allows the user to iteratively filter tickets based on input numbers.
        """
        tim = 0
        possible = []
        ended = False
        print("New Ticket Set")

        while not ended and tim != 6:
            remove = []
            # If not the first round and no possible tickets remain, end the loop
            if tim != 0 and len(possible) == 0:
                print("No Tickets")
                ended = True
                break

            # Prompt user to select a number
            try:
                tickn = int(input("Select> "))
            except ValueError:
                print("Please enter a valid integer.")
                continue
            print("\n")

            if tim == 0:
                # On the first round, filter all tickets containing the selected number
                for ticket in lottos:
                    if tickn in ticket:
                        possible.append(ticket)
            else:
                # On subsequent rounds, remove tickets that do not contain the selected number
                for ticket in possible:
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
            if tim == 6 and len(possible) > 0:
                print(f"Winning Ticket: {possible[0]}")
                sys.exit()

if __name__ == "__main__":
    main()