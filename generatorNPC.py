# generatorNPC.py
import random
from schemasNPC import (
    f_names, l_names, jobs_list, traits_list, 
    quote_data, hobbies_data, likes_data, 
    dislikes_data, goals_data, secret_data
)

def limit_val(v):
    if v < 10:
        return 10
    elif v > 95:
        return 95
    return v

def gen_stats(job, trait):
    b = random.randint(40, 85)
    if trait in ["Fearless", "Adventurous"]:
        b = b + 20
        
    i = random.randint(45, 90)
    if job in ["Detective", "Engineer", "Doctor"]:
        i = i + 15
        
    c = random.randint(35, 80)
    if trait == "Friendly":
        c = c + 20
        
    l = random.randint(30, 95)
    
    cr = random.randint(40, 88)
    if job in ["Artist", "Chef"]:
        cr = cr + 20
        
    res = {}
    res["Bravery"] = limit_val(b)
    res["Intelligence"] = limit_val(i)
    res["Charisma"] = limit_val(c)
    res["Luck"] = limit_val(l)
    res["Creativity"] = limit_val(cr)
    return res

def build_character():
    o = random.choice(jobs_list)
    p = random.choice(traits_list)
    fn = random.choice(f_names)
    ln = random.choice(l_names)
    
    char = {
        "full_name": "%s %s" % (fn, ln),
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
    return char