# lottoNumbers

This project provides a script to help you filter and check lottery tickets based on numbers you select.

## How It Works

1. **Ticket File**  
   - Store your lottery tickets in a file named `tick_nums.txt`.
   - Each line represents a ticket and should contain 6 numbers separated by spaces (e.g., `5 12 23 34 45 56`).
   - You can have any number of tickets (rows) in the file.

2. **Script Functionality**  
   - The script reads your tickets from `tick_nums.txt`.
   - You will be prompted to enter numbers one at a time.
   - After each number, the script filters and displays only the tickets that contain all the numbers you have entered so far.
   - After 6 numbers are entered, the script shows the matching ticket(s) or notifies you if no tickets match.

## Usage

1. Place your tickets in `tick_nums.txt` in the project directory.
2. Run the script:
3. Follow the prompts to enter your selected numbers.

## Notes

- The script expects each ticket to have exactly 6 numbers separated by spaces.
- You can modify the number of tickets or numbers per ticket as needed, but the script is currently set up for 6-number tickets.