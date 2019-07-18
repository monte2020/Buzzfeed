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





