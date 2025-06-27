time = int(input(f"What’s your favorite time of day? (Morning[1] / Night[2]): "))
plan = int(input(f"Pick a weekend plan: (Party[1] / Read[2] / Travel[3] / Gym[4]): "))
animal = int(input(f"Choose one animal: (Lion[1] / Owl[2] / Dolphin[3] / Cat[4]): "))

def personality_type(time, plan, animal):
    if time == 1 and plan == 4 and animal == 1:
        return f"You are a Hustler!"
    elif time == 2 and plan == 2 and animal == 2:
        return f"You are a Artist!"
    elif time == 1 and plan == 3 and animal == 3:
        return f"You are a Explorer!"
    elif time == 2 and plan == 1 and animal == 4:
        return f"You are a Vibe Seeker!"
    else:
        return f"You are a Thinker!"

ptype = personality_type(time, plan, animal)
print(ptype)