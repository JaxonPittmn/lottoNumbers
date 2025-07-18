# Lotto Numbers Filter

A Python script to help you filter and check lottery tickets based on numbers you select.

## Overview

This script reads a list of lottery tickets from a file and allows you to interactively filter them by entering numbers. After each number, only tickets containing all selected numbers remain. When 6 numbers are selected, the script displays the matching ticket.

## Features

- Reads tickets from a plain text file (`tick_nums.txt`)
- Interactive filtering based on user input
- Displays possible tickets after each selection
- Shows the matching ticket after 6 numbers are entered

## Requirements

- Python 3.x

## Usage

1. **Prepare your tickets:**
    - Create a file named `tick_nums.txt` in the same directory as the script.
    - Each line should contain exactly 6 numbers separated by spaces.  
      Example:
      ```
      5 12 23 34 45 56
      1 2 3 4 5 6
      ```

2. **Run the script:**
    ```sh
    python [Lotto_Ticket.py](http://_vscodecontentref_/0)
    ```

3. **Follow the prompts:**
    - Enter one number at a time when prompted.
    - After each entry, the script will show the remaining possible tickets.
    - After 6 numbers, the script will display the matching ticket or notify you if no tickets match.

## File Format Guidelines

- Each ticket must have exactly 6 numbers.
- Numbers must be separated by single spaces.
- No blank lines or extra spaces.
- All numbers should be valid integers.

## Example `tick_nums.txt`