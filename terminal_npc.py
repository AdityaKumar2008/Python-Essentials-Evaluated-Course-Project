# terminal_npc.py
import random

# Datasets
f_names = ["Kael", "Aria", "Liam", "Mira", "Dorian", "Elena", "Marcus", "Nyx", "Theo", "Lyra", "Adrian", "Nova", "Elias", "Rhea", "Cassian"]
l_names = ["Nightbrook", "Blackwood", "Stone", "Raven", "Ashford", "Silver", "Storm", "Vale", "Everhart", "Thorne", "Graves", "Whitlock"]
jobs_list = ["Detective", "Merchant", "Engineer", "Soldier", "Teacher", "Explorer", "Blacksmith", "Journalist", "Doctor", "Programmer", "Artist", "Chef"]
traits_list = ["Mysterious", "Friendly", "Adventurous", "Sarcastic", "Calm", "Ambitious", "Curious", "Rebellious", "Optimistic", "Cautious", "Fearless", "Introverted"]

quote_data = [
    '"Some truths are better left buried."',
    '"Every lock has a key, you just need patience to find it."',
    '"Fortune favors those who act while others hesitate."',
    '"I\'ve seen enough of the world to know nothing comes free."',
    '"A quiet shadow tells no lies."'
]

hobbies_data = ["Photography", "Reading ancient lore", "Chess", "Cooking", "Hiking", "Painting", "Gaming", "Writing stories"]
likes_data = ["Old books, Coffee, Rain, Mysteries", "Quiet places, Warm hearths, Maps", "Technology, Late-night walks, Dogs", "Ancient history, Street food, Silence"]
dislikes_data = ["Crowds, Loud noises, Liars, Cold weather", "Strict rules, Traffic, Being ignored", "Boring conversations, Being underestimated", "Unnecessary conflicts, Arrogance"]
goals_data = ["Solve an unsolved mystery", "Find a lost heirloom artifact", "Build something revolutionary", "Protect their family from hidden debts", "Explore unmapped uncharted frontiers"]

secret_data = [
    "They have been hiding a mysterious letter for years.",
    "They secretly write poetry under a dark pseudonym.",
    "They once witnessed a major crime and told no one.",
    "They hold a second fraudulent identity in a distant city.",
    "They are secretly heir to a fallen noble house."
]

icon_map = {
    "Bravery": "⚔️",
    "Intelligence": "🧠",
    "Charisma": "👤",
    "Luck": "🍀",
    "Creativity": "🎨"
}

def limit_val(v):
    if v < 10:
        return 10
    elif v > 95:
        return 95
    return v

def gen_stats(job, trait):
    b = random.randint(40, 85)
    if trait in ["Fearless", "Adventurous"]:
        b += 20
        
    i = random.randint(45, 90)
    if job in ["Detective", "Engineer", "Doctor"]:
        i += 15
        
    c = random.randint(35, 80)
    if trait == "Friendly":
        c += 20
        
    l = random.randint(30, 95)
    
    cr = random.randint(40, 88)
    if job in ["Artist", "Chef"]:
        cr += 20
        
    return {
        "Bravery": limit_val(b),
        "Intelligence": limit_val(i),
        "Charisma": limit_val(c),
        "Luck": limit_val(l),
        "Creativity": limit_val(cr)
    }

def build_character():
    o = random.choice(jobs_list)
    p = random.choice(traits_list)
    fn = random.choice(f_names)
    ln = random.choice(l_names)
    
    return {
        "full_name": f"{fn} {ln}",
        "age": random.randint(22, 58),
        "job": o,
        "personality": p,
        "quote": random.choice(quote_data),
        "likes": random.choice(likes_data),
        "dislikes": random.choice(dislikes_data),
        "goal": random.choice(goals_data),
        "hobby": random.choice(hobbies_data),
        "secret": random.choice(secret_data),
        "stats": gen_stats(o, p)
    }

def print_bar(val, max_val=100, length=20):
    filled = int(length * val // max_val)
    bar = "█" * filled + "-" * (length - filled)
    return f"[{bar}] {val}%"

def main():
    worlds = ["Fantasy", "Modern", "Cyberpunk", "Sci-Fi", "Steampunk"]
    
    print("========================================")
    print("         🧙‍♂️ TERMINAL NPC GENERATOR      ")
    print("========================================")
    
    print("\nSelect World Setting:")
    for idx, w in enumerate(worlds, 1):
        print(f"  {idx}. {w}")
    
    choice = input("\nChoose a world (1-5, default 1): ").strip()
    world_idx = int(choice) - 1 if choice.isdigit() and 1 <= int(choice) <= 5 else 0
    selected_world = worlds[world_idx]
    
    while True:
        npc = build_character()
        
        print("\n" + "="*50)
        print(f" ✦ {npc['full_name'].upper()} ✦ ")
        print("="*50)
        print(f"Age: {npc['age']}  |  Job: {npc['job']}  |  Personality: {npc['personality']}")
        print(f"World: {selected_world}")
        print(f"\nQuote: {npc['quote']}")
        print("-"*50)
        print(f"❤️ Likes:    {npc['likes']}")
        print(f"💔 Dislikes: {npc['dislikes']}")
        print(f"🎯 Goal:     {npc['goal']}")
        print(f"🎨 Hobby:    {npc['full_name']} enjoys {npc['hobby']}.")
        print(f"🔒 Secret:   {npc['secret']}")
        print("-"*50)
        print("📊 Character Stats:")
        
        stat_sum = 0
        for stat_name, val in npc["stats"].items():
            stat_sum += val
            icon = icon_map.get(stat_name, "🔹")
            print(f"  {icon} {stat_name:<12} {print_bar(val)}")
            
        avg = int(round(stat_sum / len(npc["stats"])))
        print(f"\n📈 Overall Average: {avg}/100")
        print("="*50)
        
        cmd = input("\nPress [Enter] to generate another NPC, or type 'q' to quit: ").strip().lower()
        if cmd == 'q':
            print("\nExiting NPC Generator. Goodbye!")
            break

if __name__ == "__main__":
    main()