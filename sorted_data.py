from sys import argv

script, filename = argv

openfile = open(filename)

rest_dict = {}

for line in openfile:
    line = line.strip()
    restaurant_name, rating = line.split(':')
    rest_dict[restaurant_name] = rating

for restaurant_name in sorted(rest_dict):
    print 'Restaurant "%s" is rated at %s' % (restaurant_name, rest_dict[restaurant_name])

openfile.close()