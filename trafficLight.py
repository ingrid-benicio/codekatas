def traffic_light(color):
    colors = {'green':'yellow', 'yellow':'red','red':'green'}
   
    if color in colors:

        return colors[color]
    


print(traffic_light('red'))