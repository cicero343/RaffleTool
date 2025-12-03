# **RaffleTool**

**A simple, interactive Python script to run closest-number raffles with insights and tie highlighting.**

RaffleTool allows you to:

* Assign random numbers to prizes.
* Accept submissions manually or via `.txt` import.
* Automatically determine the closest-number winner for each prize.
* Highlight ties and display additional insights sorted by distance.
  
<img width="634" height="1097" alt="raffletool2" src="https://github.com/user-attachments/assets/0e1beb2e-447e-4d11-a7a4-ac2ea6cc4440" />

---

## **Overview**

RaffleTool is a Python script designed to simplify running a raffle where winners are determined by **closest guesses** to assigned random numbers. It's ideal for giveaways, events, or testing random selection in a transparent, auditable way.

The script provides:

* Real-time display of prizes with their assigned random numbers.
* Option to submit guesses manually or import them from a text file.
* Highlighting of ties and top-N closest submissions for verification.

---

## **Features**

* **Manual or `.txt` prize entry** – easily import or type your raffle prizes.
* **Random number assignment (1–100)** – unique for each prize.
* **Manual or `.txt` submissions** – flexible entry handling.
* **Closest-number winner selection** – automatically determines winners.
* **Tie highlighting and insights** – see who came closest even if they didn’t win.
* **Terminal-friendly display** – prizes and winners highlighted with bold formatting.

---

## **Installation**

RaffleTool requires **Python 3.x**.

1. Clone or download this repository:

```bash
git clone https://github.com/yourusername/RaffleTool.git
```

2. Navigate to the repository folder:

```bash
cd RaffleTool
```

3. Run the script:

```bash
python RaffleTool.py
```

---

## **Usage**

1. Select how to enter your prizes: manually or via `.txt` file.
2. Review the prizes along with their randomly assigned numbers.
3. Enter the submissions (name + number) manually or via `.txt` file.
4. View the **raffle results** in the terminal, with prizes and winners highlighted.
5. Optionally, view additional insights showing the top-N closest submissions and ties.

**Example output:**

```
✅ Prizes with assigned random numbers:
1) 150g                → Random Number: 73
2) 100g                → Random Number: 51
...
=== RAFFLE RESULTS ===
1) 150g                (73) → Winner: Riven (69) ⚠️ Ties: Huko Yappingtail
2) 100g                (51) → Winner: Nyah (51)
...
```

---

## **License**

This project is licensed under the **MIT License** – see the LICENSE file for details.

---
