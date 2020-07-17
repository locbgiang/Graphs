from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
go_back = {
    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e'
}

room = {}
visited = set()
path = []

while len(visited) != len(room_graph):              # keep running this while visited is lower than total room
    roomId = player.current_room.id
    if roomId not in visited:                                       # if the current room is not in visited
        visited.add(roomId)                                           # add it to visited 
        directions = player.current_room.get_exits()                 
        room[roomId] = directions                                   # create the possible directions

    while len(room[roomId]) >= 0:                                  
        if len(room[roomId]) > 0:                                  # if there is still a direction to go on
            move = room[roomId].pop()                               # move in that direction and pop it from hash
            if player.current_room.get_room_in_direction(move).id not in visited:               # if the new room is not in memory
                path.append(move)                                                   #save the move to path
                traversal_path.append(move)              #save the movement
                player.travel(move)                                                # move the player in that direction 
                break
        elif len(room[roomId]) == 0:                                        # if there are no new direction to go on
            back_room = path.pop()                                       # go back to the previous room
            traversal_path.append(go_back[back_room])         #save the movement
            player.travel(go_back[back_room])                # move the player
            break




# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


'''
#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
'''