import heapq
import collections

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
    
        events = []
        for l, r, h in buildings:
            events.append((l, -h))  
            events.append((r, h))   


        events.sort()

        skyline = []

        live_buildings = [0]

        height_counts = collections.defaultdict(int)
        height_counts[0] = 1 

        prev_max_height = 0 
        for x, h_val in events:
            if h_val < 0: 
                height = -h_val
                heapq.heappush(live_buildings, -height)
                height_counts[height] += 1
            else:  
                height = h_val
                height_counts[height] -= 1

            while height_counts[-live_buildings[0]] == 0:
                heapq.heappop(live_buildings)

            current_max_height = -live_buildings[0] 
            if current_max_height != prev_max_height:
                skyline.append([x, current_max_height])
                prev_max_height = current_max_height

        return skyline