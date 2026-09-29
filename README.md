# Python-Essentials---Evaluated-Course-Project

NPC Generator

A flexible Python project built to help game developers, writers, and dungeon masters create rich, randomized Non-Player Characters (NPCs) instantly—without having to manually write out names, backstories, traits, and balanced statistics every time. It combines procedural generation rules to output a complete character profile complete with quotes, likes, dislikes, goals, secrets, and core stats.

What It Does

* **Dual Interface Options:** Run your choice of the structured terminal console (`main.py` / `terminal_npc.py`) or the interactive web app with graphical charts.
* **Procedural Stat Balancing:** Calculates statistics (Bravery, Intelligence, Charisma, Luck, Creativity) dynamically based on the character's profession and personality traits.
* **Clean, Separated Code:** Organized into focused modules so you can easily tweak datasets or generation logic without cluttering the interface code.

Built With & Prerequisites

Depending on which mode you choose to run, your setup will use one of the following:

* **For the Streamlit Web UI (with Visualizations):** 
  * Language & Frameworks: Python 3, Streamlit, Matplotlib, NumPy
  * Installation: `pip install streamlit matplotlib numpy`
* **For the Pure Terminal / Console Version (`main.py` or `terminal_npc.py`):** 
  * Language: Python 3 (runs entirely on native libraries like `random`—no external packages or `pip install` required)

Project Structure

npc_generator/

├── schemes_db.py      # Character datasets (names, jobs, traits, quotes, and lore data)

├── validator.py       # Logic that handles procedural stat generation and boundaries

├── main.py            # CLI runner, menus, and user prompt handling

├── terminal_npc.py    # Standalone alternative CLI runner for quick terminal execution

├── statement.md       # Problem statement and scope definition

└── README.md          # Quickstart and overview

To run GUI
* streamlit run mainNPC.py    OR    python -m streamlit run mainNPC.py
