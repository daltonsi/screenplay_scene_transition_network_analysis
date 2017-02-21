import regex as re
from collections import OrderedDict

movies = ['titanic',
          'star_wars',
          'empire_strikes_back']
for movie in movies:
    file = open('./input/' + movie + '.txt', 'r')

    scenes = []
    characters = OrderedDict()
    bool = False
    first_scene = True
    scene_count = 1
    with open('./output/' + movie + '_results.txt', 'w') as f:
        for line in file:
            result = re.search(r'((?:EXT|INT).+)', line)
            if result:
                if first_scene:
                    first_scene = False
                else:
                    if characters[scene]:
                        f.write(str(scene_count) + ':\t' + str(scene) + ':\t' + str(characters[scene]) + '\n')
                        scene_count += 1
                    else:
                        f.write(str(scene_count) + ':\t' + str(scene) + ':\t' + 'None\n')
                        scene_count += 1
                bool = True
                scene = re.sub(r'\s+\d+', '', result.group(1))
                scenes.append(scene)
                characters[scene] = []
            elif bool:
                result2 = re.search('^(?:\s{5}|\s{4})([A-Z]+)', line)
                if result2:
                    character = re.sub(r'\s{5}', '', result2.group(1))
                    characters[scene].append(character)