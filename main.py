import random
from npc_core.schemes_db import NAMES, JOBS, TRAITS, QUOTES, SECRETS
from npc_core.validator import generate_stats

def build_npc():
    npc = {
        "Name": random.choice(NAMES),
        "Job": random.choice(JOBS),
        "Trait": random.choice(TRAITS),
        "Quote": random.choice(QUOTES),
        "Secret": random.choice(SECRETS)
    }
    npc["Stats"] = generate_stats(npc["Job"], npc["Trait"])
    return npc

if __name__ == "__main__":
    print("\n--- Procedural NPC Generated ---")
    npc = build_npc()
    for key, value in npc.items():
        if key == "Stats":
            print("\nStats:")
            for stat, val in value.items():
                print(f"  - {stat}: {val}")
        else:
            print(f"{key}: {value}")
    print("--------------------------------\n")