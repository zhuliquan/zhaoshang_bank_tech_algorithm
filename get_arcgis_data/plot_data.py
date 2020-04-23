import json
import matplotlib.pyplot as plt
area = []
for i in range(1, 5):
    with open("./{0}.json".format(i)) as f:
        d = json.load(f)
    for j in range(2):
        locations = d["saPolygons"]["features"][j]["geometry"]["rings"][0]
        print(locations)
        x = [location[0] if location[0] < 0 else location[1] for location in locations]
        y = [location[0] if location[0] > 0 else location[1] for location in locations]
        plt.plot(x, y, 'b-', linewidth=2)

plt.show()
        
         