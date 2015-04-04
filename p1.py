# Thomas Milne-Jones and Brett Hatch
# tmlinejo and bhatch
# programming assignment 1

from p1_support import load_level, show_level
from math import sqrt
from heapq import heappush, heappop

def dijkstras_shortest_path(src, dst, graph, adj):
   if src == dst:
      return [src]
   queue = []
   dist = {src: 0}
   parent = {src: None}
   heappush(queue, (0, src))
   solution = []
   
   while queue:
      weight, current = heappop(queue)
      dist[current] = weight
      paths = adj(graph, current)
      for path in paths:
         weight, neighbor = path
         alt = dist[current] + weight
         if neighbor not in dist or alt < dist[neighbor]:
            parent[neighbor] = current
            dist[neighbor] = alt
            if neighbor == dst: # destination found, create list and return
               current = neighbor
               while not current is None:
                  solution.append(current)
                  current = parent[current]
               solution.reverse()
               return solution
            if neighbor not in queue: # add to queue if not already found
               heappush(queue, (alt, neighbor))
      

def navigation_edges(level, cell):
   paths = []
   x, y = cell
   for dx in [-1,0,1]:
      for dy in [-1,0,1]:
         nextCell = ((x+dx), (y+dy))
         if nextCell in level['spaces'] and nextCell != cell:
            paths.append((sqrt(dx*dx+dy*dy), nextCell))
      
   return paths

def test_route(filename, src_waypoint, dst_waypoint):
	level = load_level(filename)

	show_level(level)

	src = level['waypoints'][src_waypoint]
	dst = level['waypoints'][dst_waypoint]

	path = dijkstras_shortest_path(src, dst, level, navigation_edges)

	if path:
		show_level(level, path)
	else:
		print "No path possible!"

if __name__ ==  '__main__':
	import sys
	_, filename, src_waypoint, dst_waypoint = sys.argv
	test_route(filename, src_waypoint, dst_waypoint)
