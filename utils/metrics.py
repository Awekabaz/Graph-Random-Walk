def l1_distance(vector1, vector2):
    if type(vector1) == 'dict':
        return sum([abs(vector1[n] - vector2[n]) for n in vector1])

    return sum([abs(vector1[n] - vector2[n]) for n in range(len(vector1))])
