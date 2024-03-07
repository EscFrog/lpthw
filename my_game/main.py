from sys import exit
from random import randint
from textwrap import dedent


class Engine(object):

  def __init__(self, scene_map):
    self.scene_map = scene_map

  def play(self):
    current_scene = self.scene_map.opening_scene()
    last_scene = self.scene_map.next_scene('finished')

    while current_scene != last_scene:
      next_scene_name = current_scene.enter()
      current_scene = self.scene_map.next_scene(next_scene_name)

    #be sure to print out the last scene
    current_scene.enter()


class Scene(object):

  def enter(self):
    print("This scene is not yet confitured.")
    print("Subclass it and implement enter().")
    exit(1)


class Map(object):

    scenes = {
    'central_corridor': CentralCorridor(),
    'laser_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'death': Death(),
    'finished': Finished(),
  }

  def __init__(self, start_scene):
    self.start_scene = start_scene

  def next_scene(self, scene_name):
    val = Map.scenes.get(scene_name)
    return val

  def opening_scene(self):
    return self.next_scene(self.start_scene)


class Death(Scene):

  quips = [
    "You died. You kinda suck at this.",
    "Your Mom would be proud... if she were smarter.",
    "Such a luser.",
    "I have a small puppy that's better at this.",
    "You're worse than your Dad's jokes."
  ]

  def enter(self):
    print(Death.quips[randint(0, len(self.quips)-1)])
    exit(1)


class CentralCorridor(Scene):

  def enter(self):
    print(dedent("""
      The Gothons of Planet Percal #25 have invaded your ship and
      destroyed your entire crew. You are the last surviving
      memeber and your last mission is to get the neutron destruct
      bomb from the Weapons Armory, put it tin the bridge, and
      blow the ship up after getting into an escape pod.

      You're running down the central corridor to the Weapons
      Armory when a Gothon jumps out, red scaly skin, dark grimy
      teeth, and evil clown costume flowing around his hate
      filled body. He's blocking the door to the Armory and
      about to pull a weapon to blast you.
    """))
    
    action = input("> ")

    if action == "shoot!":
      print(dedent("""
        Quick on the draw you yank out your blaster and fire
        it at the Gothon. His clown costume is flowing and
        moving around his body, which throws off your aim.
        Your laser hets his costume but misses him entirely.
        This completely ruins his brand new costume his mother
        bought him, which makes him fly into an insane rage
        and blast you repeatedly in the face until you are
        dead. Then he eats you.      
      """))
      return 'death'
    
    elif action == "dodge!":
      print(dedent("""
        Like a world class boxer you dodge, weave, slip and
        slide right as the Gothon's blaster cranks a laser
        past your head. In the middle of your artful dodge
        your foot slips and you bang your head on the metal
        wall and pass out. You wake up shortly after only to
        die as the Gothon stomps on you head and eats you.
      """))
      return 'death'

    elif action == "tell a joke":
      print(dedent("""
        Lucky for you they made you learn Gothon insults in
        the academy. You tell the one Gothon joke you know:
        Lbhe zbgure vf fb sng, jura fur fvgf nebhaq qur ubhfr,
        fur fvgf nbhaq qur ubhfr. The Gothon stops, tries move.
        While he's laughing you run up and shoot him square in
        the head putting him down, then jump through the
        Weapon Amory door.
        """))
      return 'laser_weapon_armory'

    else:
      print("DOES NOT COMPUTE!")
      return 'central_corridor'


