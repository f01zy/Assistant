import winsound

def say(filename):
    winsound.PlaySound(f"sounds/jarvis/{filename}" , winsound.SND_ALIAS)