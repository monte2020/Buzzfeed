def soccer_quiz(position, goal, mindset, team, best):
    messi_score=0
    modric_score=0
    van_score=0
    if position == "Striker":
        messi_score += 1
    elif position == "Centermid":
        modric_score += 1
    elif position == "Centerback":
        van_score += 1
    elif goal == "Dribble past the goalie":
        messi_score += 1
    elif goal == "Pass the ball into the goal":
        modric_score += 1
    elif goal == "Header":
        van_score += 1
    elif mindset == "Be the difference":
        messi_score += 1
    elif mindset == "Help the game flow":
        modric_score += 1
    elif mindset == "Defense":
        van_score += 1 
    elif team == "Barcelona":
        messi_score += 1
    elif team == "Madrid":
        modric_score += 1
    elif team == "Liverpool":
        van_score += 1
    elif best == "Quick as lightining":
        messi_score += 1
    elif best == "Run for miles":
        modric_score += 1
    elif best == "Human tank":
        van_score += 1
    if messi_score > modric_score and messi_score > van_score:
        return "You are Messi"
    elif modric_score > messi_score and modric_score > van_score:
        return "You are Modric"
    elif van_score > messi_score and van_score > modric_score:
        return "You are Van Dijk"
    elif messi_score == modric_score:
        return "You are messi"
    elif modric_score == van_score:
        return "You are Modric"
    elif messi_score == van_score:
        return "You are Van Dijk"


def chain_quiz(type1, meat, color, when1, age):
    burg_score=0
    kfc_score=0
    taco_score=0
    if type1 == "Traditional American":
        burg_score += 1
    elif type1 == "Fried":
        kfc_score += 1
    elif type1 == "Mexican":
        taco_score += 1
    elif meat == "Beef":
        burg_score += 1
    elif meat == "Chicken":
        kfc_score += 1
    elif meat == "Don't care as long as it's in a taco":
        taco_score += 1
    elif color == "Yellowe":
        burg_score += 1
    elif color == "Red":
        kfc_score += 1
    elif color == "Purple":
        taco_score += 1 
    elif when1 == "Coming home":
        burg_score += 1
    elif when1 == "Whenever":
        kfc_score += 1
    elif when1 == "On a road trip":
        taco_score += 1
    elif age == "4-10":
        kfc_score += 1
    elif age == "12-16":
        taco_score += 1
    elif age == "1-99":
        burg_score += 1
    if burg_score > kfc_score and burg_score > taco_score:
        return "You are Burger King"
    elif kfc_score > burg_score and kfc_score > taco_score:
        return "You are KFC"
    elif taco_score > burg_score and taco_score > kfc_score:
        return "You are Taco Bell"
    elif burg_score == kfc_score:
        return "You are Burger King"
    elif kfc_score == taco_score:
        return "You are KFC"
    elif burg_score == taco_score:
        return "You are Taco Bell"


def genre_quiz(style, why, feel, where, artist):
    jazz_score=0
    rock_score=0
    pop_score=0
    if style == "Make your own style":
        jazz_score += 1
    elif style == "Identify with past generations":
        rock_score += 1
    elif style == "Conform with the masses":
        pop_score += 1
    elif why == "Appreciating background music":
        jazz_score += 1
    elif why == "For a good suggestion in a family parties":
        rock_score += 1
    elif why == "Just listening to the radio":
        pop_score += 1
    elif feel == "Inspired":
        jazz_score += 1
    elif feel == "Nostalgic":
        rock_score += 1
    elif feel == "Depends on my mood":
        pop_score += 1 
    elif where == "Anywhere with some company":
        jazz_score += 1
    elif where == "Road trip":
        rock_score += 1
    elif where == "In my room":
        pop_score += 1
    elif artist == "Louis Daniel Armstrong":
        jazz_score += 1
    elif artist == "The Beatles":
        rock_score += 1
    elif artist == "Billie Eillish":
        pop_score += 1
    if jazz_score > rock_score and jazz_score > pop_score:
        return "You are jazz"
    elif rock_score > jazz_score and rock_score > pop_score:
        return "You are classic rock"
    elif pop_score > jazz_score and pop_score > rock_score:
        return "You are pop music"
    elif jazz_score == rock_score:
        return "You are jazz"
    elif rock_score == pop_score:
        return "You are classic rock"
    elif jazz_score == pop_score:
        return "You are pop music"


