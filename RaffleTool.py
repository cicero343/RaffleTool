# -----------------------------------------
#  Raffle Script with Manual Input or .txt Import
#  Closest-number, 1 prize per player
#  Includes insights for verification and tie highlighting
# -----------------------------------------

import os
import random

# ----------------------------------------------------------
# ASCII Title
# ----------------------------------------------------------
print(r"""
█████▄   ▄▄▄  ▄▄▄▄▄ ▄▄▄▄▄ ▄▄    ▄▄▄▄▄ ██████ ▄▄▄   ▄▄▄  ▄▄
██▄▄██▄ ██▀██ ██▄▄  ██▄▄  ██    ██▄▄    ██  ██▀██ ██▀██ ██
██   ██ ██▀██ ██    ██    ██▄▄▄ ██▄▄▄   ██  ▀███▀ ▀███▀ ██▄▄▄
""")

# ----------------------------------------------------------
# Prize Setup
# ----------------------------------------------------------
print("\nWelcome to RaffleTool! Please enter the prizes for the raffle.")
print("[1] Manual input")
print("[2] Import from .txt file (1 prize per line, max 100 chars)")

choice = input("\nEnter 1 or 2: ").strip()
prizes_list = []

if choice == "1":
    print("\nEnter each prize on a separate line. Type 'done' when finished.")
    while True:
        prize = input(f"Prize {len(prizes_list)+1}: ").strip()
        if prize.lower() == "done":
            break
        if len(prize) == 0:
            print("⚠️ Prize cannot be empty, try again.")
            continue
        if len(prize) > 100:
            print("⚠️ Prize name too long (max 100 characters).")
            continue
        prizes_list.append(prize)

elif choice == "2":
    print("\nTip: You can type the filename OR drag & drop the file into this window.")
    filename = input("\nEnter the filename (e.g., prizes.txt): ").strip().strip('"')
    filename = os.path.expanduser(filename)
    if not os.path.isfile(filename):
        print(f"\n❌ File not found: {filename}")
        exit()

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"\nImporting {len(lines)} prizes from {filename}...\n")
    for line_num, line in enumerate(lines, start=1):
        prize = line.strip()
        if not prize:
            continue
        if len(prize) > 100:
            print(f"⚠️ Prize too long on line {line_num}, skipped.")
            continue
        prizes_list.append(prize)
else:
    print("\nInvalid choice. Exiting.")
    exit()

# ----------------------------------------------------------
# Assign random numbers to prizes (1–100, unique)
# ----------------------------------------------------------
available_numbers = list(range(1, 101))
random.shuffle(available_numbers)

prizes_with_numbers = []  # list of tuples: (prize_name, prize_number)
for prize_name in prizes_list:
    if not available_numbers:
        raise Exception("Not enough random numbers for prizes!")
    prize_number = available_numbers.pop()
    prizes_with_numbers.append((prize_name, prize_number))

# ----------------------------------------------------------
# Display prizes with assigned random numbers (single table)
# ----------------------------------------------------------
print("\n✅ Prizes with assigned random numbers:\n")
max_length = max(len(p) for p, n in prizes_with_numbers)
for i, (prize_name, prize_number) in enumerate(prizes_with_numbers, start=1):
    # Bold the prize name for terminal visibility
    print(f"{i:>2}) \033[1m{prize_name:<{max_length}}\033[0m → Random Number: {prize_number}")

print("\nNow enter submissions with your names and numbers...\n")

# ----------------------------------------------------------
# Submissions Input
# ----------------------------------------------------------
print("[1] Manual input")
print("[2] Import from .txt file (format: name, number), 1 per line")
choice = input("\nEnter 1 or 2: ").strip()

submissions = []

# Manual input
if choice == "1":
    print("\nEnter submissions in the format: name, number (type 'done' to finish)")
    i = 1
    while True:
        entry = input(f"Submission {i}: ").strip()
        if entry.lower() == "done":
            break
        try:
            name, number = entry.split(",")
            submissions.append((name.strip(), int(number.strip())))
            i += 1
        except:
            print("Invalid format! Please use: name, number")

# Import from file
elif choice == "2":
    print("\nTip: You can type the filename OR drag & drop the file into this window.")
    filename = input("\nEnter the filename (e.g., entries.txt): ").strip().strip('"')
    filename = os.path.expanduser(filename)
    if not os.path.isfile(filename):
        print(f"\n❌ File not found: {filename}")
        exit()

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"\nImporting {len(lines)} lines from {filename}...\n")
    for line_num, line in enumerate(lines, start=1):
        line = line.strip()
        if not line:
            continue
        try:
            name, number = line.split(",")
            submissions.append((name.strip(), int(number.strip())))
        except:
            print(f"⚠️  Skipped invalid line {line_num}: '{line}'")

# ----------------------------------------------------------
# Function to find closest winner
# ----------------------------------------------------------
def find_closest_winner(prize_number, submissions, winners_set):
    closest_distance = float("inf")
    winner = None
    winner_number = None
    distances = []
    for submitter, number in submissions:
        if submitter in winners_set:
            continue
        distance = abs(prize_number - number)
        distances.append((submitter, number, distance))
        if distance < closest_distance:
            closest_distance = distance
            winner = submitter
            winner_number = number
    ties = [s for s, n, d in distances if d == closest_distance and s != winner]
    return winner, winner_number, distances, ties

# ----------------------------------------------------------
# Assign prizes and show results with bold and aligned output
# ----------------------------------------------------------
winners_set = set()
prize_winner_info = {}  # store data for insights

print("\n=== RAFFLE RESULTS ===\n")

# Pre-calculate maximum lengths for alignment
max_prize_len = max(len(p) for p, n in prizes_with_numbers)
max_winner_len = 0
for prize_name, prize_number in prizes_with_numbers:
    winner, winner_number, distances, ties = find_closest_winner(prize_number, submissions, winners_set)
    if winner:
        max_winner_len = max(max_winner_len, len(winner))

# Assign prizes and print nicely
for i, (prize_name, prize_number) in enumerate(prizes_with_numbers, start=1):
    winner, winner_number, distances, ties = find_closest_winner(prize_number, submissions, winners_set)
    prize_winner_info[(prize_name, i)] = {
        "number": prize_number,
        "winner": winner,
        "winner_number": winner_number,
        "distances": distances,
        "ties": ties
    }

    # Bold prize
    prize_text = f"\033[1m{prize_name:<{max_prize_len}}\033[0m"
    
    if winner:
        winners_set.add(winner)
        winner_text = f"\033[1m{winner:<{max_winner_len}}\033[0m ({winner_number})"
        tie_text = f" ⚠️ Ties: {', '.join(ties)}" if ties else ""
    else:
        winner_text = "No eligible winner"
        tie_text = ""

    print(f"{i:>2}) {prize_text} ({prize_number:>3}) → Winner: {winner_text}{tie_text}")

# ----------------------------------------------------------
# Show additional insights (top-N closest submissions)
# ----------------------------------------------------------
show_insights = input("\nShow more insights? (Y/N): ").strip().lower()
if show_insights == "y":
    TOP_N = 3  # number of closest submissions to show per prize
    print("\n=== INSIGHTS ===\n")
    for (prize_name, idx), info in prize_winner_info.items():
        print(f"Prize: {prize_name} ({info['number']})")
        sorted_distances = sorted(info["distances"], key=lambda x: x[2])
        for submitter, number, distance in sorted_distances[:TOP_N]:
            tie_marker = " ⚠️" if submitter in info["ties"] else ""
            print(f"  {submitter} ({number}) → Distance: {distance}{tie_marker}")
        print()
