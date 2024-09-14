from pprint import pprint
from models.house import House
from models.object import *
from models.paint import *
from models.color import *
from models.style import *

from conditions.simple import *

house = House()
house.get_random()
print(house.get_display())

conds = generate_conditions_empty_or_not_empty(house)
pprint(conds)

conds = generate_conditions_the_house_contains(house)
pprint(conds)

conds = generate_conditions_only_room_empty(house)
pprint(conds)

conds = generate_conditions_no_of_empty_rooms(house)
pprint(conds)
