import math

#rotate function - needed help for this :(
def rotate(vector, angle):
    x, y = vector
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    return (
        x * cos_a - y * sin_a,
        x * sin_a + y * cos_a
    )

def map(n, start1, stop1, start2, stop2):
    newval = (n - start1) / (stop1 - start1) * (stop2 - start2) + start2
    if newval > stop2:
        return stop2
    elif newval < start2:
        return start2
    else:
        return newval
