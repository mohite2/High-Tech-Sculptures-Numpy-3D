import numpy as np
import importlib
from scipy.ndimage import center_of_mass
from typing import List

def are_rotations_unique(list_of_rotations: List[List[dict]], verbose=True) -> bool:
    """Given a list of list of 3D rotation combinations suitable for using with np.rot90()
    and as returned from the get_orientations_possible() function, determine whether any
    of the rotations are equivalent, and discard the duplicates.

    The purpose is to detect situations where a combination of rotations would produce either
    the original unmodified array or the same orientation as any previous one in the list.

    NOTE: This function is already complete! It is provided as an example of rotation
    calculations, good Doctests, and it could be useful to you as part of your solution.

    :param list_of_rotations: a list, such as returned by get_orientations_possible()
    :param verbose: if True, will print details to console, otherwise silent.
    :return: True, if all listed rotation combinations produce distinct orientations.

    >>> x = [[{'k': 4, 'axes': (0, 1)}]]  # 4x90 degrees is a full rotation
    >>> are_rotations_unique(x)
    False
    >>> x = [[{'k': 2, 'axes': (0, 1)}, {'k': 2, 'axes': (0, 1)}]]  # also a full rotation
    >>> are_rotations_unique(x)
    False
    >>> y1 = [[{'k': 3, 'axes': (1, 2)}], [{'k': 1, 'axes': (0, 1)}, {'k': 1, 'axes': (2, 0)}]]
    >>> are_rotations_unique(y1)
    True
    >>> y2 = y1 + [[{'k': 1, 'axes': (1, 2)}, {'k': 3, 'axes': (1, 0)}]]  # equiv. to earlier
    >>> are_rotations_unique(y2, verbose=True)
    combination #1: [{'k': 3, 'axes': (1, 2)}] ok.
    combination #2: [{'k': 1, 'axes': (0, 1)}, {'k': 1, 'axes': (2, 0)}] ok.
    combination #3: [{'k': 1, 'axes': (1, 2)}, {'k': 3, 'axes': (1, 0)}] not unique.
    it results in the same array as combination 2
    False
    """
    # create a small cube to try all the input rotations. It has unique values so that
    #  no distinct rotations could create an equivalent array by accident.
    cube = np.arange(0, 27).reshape((3, 3, 3))
    #why having this cube?
    # Note: In the code below, the arrays must be appended to the orientations_seen
    #  list in string form, because Numpy would otherwise misunderstand the intention
    #  of the if ... in orientations_seen expression.

    orientations_seen = [cube.tostring()]  # record the original

    count = 0
    for combo in list_of_rotations:
        count += 1
        if verbose:
            print('combination #{}: {}'.format(count, combo), end='')

        r = cube  # start with a view of cube unmodified for comparison
        for r90 in combo:  # apply all the rotations given in this combination
            r = np.rot90(r, k=r90['k'], axes=r90['axes'])
            print('r90',r90)
            print('r',r)
        if r.tostring() in orientations_seen:
            if verbose:
                print(' not unique.')
                if r.tostring() == cube.tostring():
                    print('it results in the original 3d array.')
                else:
                    print('it results in the same array as combination',
                          orientations_seen.index(r.tostring()))
            return False
        else:
            if verbose:
                print(' ok.')
        orientations_seen.append(r.tostring())
    return True

poss = [
        [{'k': 1, 'axes': (0, 1)}],  # 1-axis rotations:
        [{'k': 2, 'axes': (0, 1)}],
        [{'k': 3, 'axes': (0, 1)}],
        [{'k': 1, 'axes': (0, 2)}],
        [{'k': 2, 'axes': (0, 2)}],
        [{'k': 3, 'axes': (0, 2)}],
        [{'k': 1, 'axes': (1, 2)}],
        [{'k': 2, 'axes': (1, 2)}],
        [{'k': 3, 'axes': (1, 2)}],
        [{'k': 1, 'axes': (0, 1)}, {'k': 1, 'axes': (0, 2)}],  # 2-axis rotations:
        [{'k': 1, 'axes': (0, 1)}, {'k': 2, 'axes': (0, 2)}],
        [{'k': 1, 'axes': (0, 1)}, {'k': 3, 'axes': (0, 2)}],
        [{'k': 2, 'axes': (0, 1)}, {'k': 1, 'axes': (0, 2)}],
        [{'k': 2, 'axes': (0, 1)}, {'k': 3, 'axes': (0, 2)}],
        [{'k': 3, 'axes': (0, 1)}, {'k': 1, 'axes': (0, 2)}],
        [{'k': 3, 'axes': (0, 1)}, {'k': 2, 'axes': (0, 2)}],
        [{'k': 3, 'axes': (0, 1)}, {'k': 3, 'axes': (0, 2)}],
        [{'k': 1, 'axes': (1, 2)}, {'k': 1, 'axes': (0, 2)}],
        [{'k': 1, 'axes': (1, 2)}, {'k': 2, 'axes': (0, 2)}],
        [{'k': 1, 'axes': (1, 2)}, {'k': 3, 'axes': (0, 2)}],
        [{'k': 3, 'axes': (1, 2)}, {'k': 1, 'axes': (0, 2)}],
        [{'k': 3, 'axes': (1, 2)}, {'k': 2, 'axes': (0, 2)}],
        [{'k': 3, 'axes': (1, 2)}, {'k': 3, 'axes': (0, 2)}],
    ]
for x in poss:
    result=are_rotations_unique([x])
#print(result)
