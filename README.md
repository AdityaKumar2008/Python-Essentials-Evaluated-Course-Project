# Procedural NPC Generator

Welcome to my repository. This is my original project submission for the VITyarthi "Build Your Own Project" flipped course evaluation.

I have built a Python-based console application to solve a common game development challenge: generating randomized, balanced Non-Player Characters (NPCs) instantly without manual writing[cite: 1].

Since this app emphasizes local control, lightweight execution, and zero setup hassle, it runs completely in the terminal environment using standard Python libraries[cite: 1, 4].

**Author:** Aditya Kumar (26BAI10218)

---

## Project Overview
This project provides a robust command-line character generator that dynamically calculates core attributes (Bravery, Intelligence, Charisma, Luck, Creativity) using job and trait modifiers while outputting unique lore profiles[cite: 1].

## Features & Functional Modules
Per the course criteria, the application is divided into three distinct functional modules[cite: 2, 4]:
*   **Character Dataset Module (`npc_core/schemes_db.py`):** Stores memory pools for character names, professions, traits, quotes, and secrets[cite: 1].
*   **Procedural Balancing Module (`npc_core/validator.py`):** Runs dynamic stat adjustment rules and bounds all outputs within a strict scale[cite: 1].
*   **Interactive CLI Runner (`main.py`):** Interactive terminal loop with formatted profile cards and ASCII attribute bar charts[cite: 1, 4].

## Technologies Used
*   **Language:** Python 3 (Modular Architecture)[cite: 1, 2, 4]
*   **Core Libraries:** `random` (Standard Library)[cite: 1, 4]
*   **Dependencies:** None. Built purely on standard Python for zero-configuration deployments.

## How to Install and Run

1. Clone this repository to your local machine[cite: 2, 4]:
   ```bash
   git clone https://github.com/AdityaKumar2008/Python-Essentials-Evaluated-Course-Project.git
   ```
2. Navigate into the project root folder:
   ```bash
   cd Python-Essentials-Evaluated-Course-Project
   ```
3. Execute the entry point script:
   ```bash
   python main.py
   ```