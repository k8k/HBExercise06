from sys import argv

script, filename = argv

openfile = open(filename)

rest_dict = {}

for line in openfile:
    line = line.strip()
    restaurant_name, rating = line.split(':')
    rest_dict[restaurant_name] = rating

# for restaurant_name in sorted(rest_dict):
#     print 'Restaurant "%s" is rated at %s' % (restaurant_name, rest_dict[restaurant_name])

#for i in sorted(rest_dict.keys()):
 #   print 'Restaurant "%s" is rated %s' % (i, rest_dict[i])

sorted_values = sorted(rest_dict.values())
sorted_restnames = sorted(rest_dict, key=rest_dict.get)

sorted_values = sorted_values[::-1]
sorted_restnames = sorted_restnames[::-1]

for item in sorted_restnames:
    print 'Restaurant "%s" is rated %s' % (item, sorted_values[sorted_restnames.index(item)])

openfile.close()