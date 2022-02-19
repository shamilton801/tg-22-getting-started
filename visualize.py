from scotland_yard import Scotland_yard
from hider import Hider
from cyberchase import Match

# Lower frame_delay to increase animation speed (and vice-versa)
match = Match(Scotland_yard, Hider, games=1, render=True, frame_delay=0.2)
match.run()