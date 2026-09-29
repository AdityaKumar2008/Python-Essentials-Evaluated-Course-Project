# Problem Statement & Scope

## Problem Statement
Game developers and dungeon masters frequently experience creative fatigue when manually generating background characters. There is a need for an automated, zero-dependency CLI tool that outputs balanced, lore-friendly NPCs instantly to maintain workflow momentum.

## Scope & Target Users
* **Target Users:** Tabletop Dungeon Masters (D&D/Pathfinder), Game Developers, Creative Writers[cite: 1, 2].
* **Scope:** The project procedurally generates complete NPC profiles—including names, professions, core traits, lore secrets, and dynamic stat calculations bounded between 1 and 20.

## Functional & Non-Functional Modules
1. **Datasets Module (`npc_core/schemes_db.py`):** Structured memory array for prompt pools[cite: 1].
2. **Procedural Logic (`npc_core/validator.py`):** Modifies and bounds core stats based on job and personality matrix[cite: 1].
3. **CLI Runner (`main.py`):** Interactive menu rendering ASCII stat bars in terminal[cite: 1, 4].