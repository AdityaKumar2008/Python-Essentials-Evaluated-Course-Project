import random

def generate_stats(job: str, trait: str) -> dict:
    stats = {"Bravery": 10, "Intelligence": 10, "Charisma": 10, "Luck": 10, "Creativity": 10}
    
    if job == "Mage": stats["Intelligence"] += 5; stats["Creativity"] += 3
    elif job == "Rogue": stats["Luck"] += 4; stats["Charisma"] += 2
    elif job == "Paladin": stats["Bravery"] += 5; stats["Charisma"] += 3
    
    if trait == "Brave": stats["Bravery"] += 4
    elif trait == "Cowardly": stats["Bravery"] -= 5; stats["Luck"] += 2
    elif trait == "Cunning": stats["Intelligence"] += 3; stats["Charisma"] += 2
    
    for key in stats:
        stats[key] = max(1, min(20, stats[key] + random.randint(-2, 3)))
        
    return stats