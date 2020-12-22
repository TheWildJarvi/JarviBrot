from fxpmath import Fxp
import sys
file1 = open("768pal3.hex", "w")
EPSILON = sys.float_info.epsilon  # Smallest possible difference.

def convert_to_rgb(maxval, val, colors):
    i_f = float(val) / float(maxval) * (len(colors) - 1)
    i, f = int(i_f // 1), i_f % 1  # Split into whole & fractional parts.
    # Does it fall exactly on one of the color points?
    if f < EPSILON:
        return colors[i]
    else:  # Otherwise return a color within the range between them.
        (r1, g1, b1), (r2, g2, b2) = colors[i], colors[i + 1]
        return int(r1 + f * (r2 - r1)), int(g1 + f * (g2 - g1)), int(b1 + f * (b2 - b1))

maxval = 767
colors = [(0, 15, 15), (0,0,15), (15, 0, 15)]  # [Beginning, Middle , End]
print('  Val       R    G    B')
file1.write('v2.0 raw')
for i in range(maxval+1):
    r, g, b = convert_to_rgb(maxval, i, colors)
    fxpred = (Fxp(r, 0, 16, 0))
    fxpgreen = (Fxp(g, 0, 16, 0))
    fxpblue = (Fxp(b, 0, 16, 0))
    const = (Fxp(1, 0, 16, 0))

    fxpword = Fxp(None, 0, 16, 0)
    fxpword.equal( ((const & 0x0001)<<15) | ((fxpred & 0x001f )<< 10)| ((fxpgreen & 0x001f )<< 5) | ((fxpblue & 0x001f )))

    print('{:3d} -> ({:3d}, {:3d}, {:3d})'.format(i, r, g, b))

    file1.write('\n' + str(fxpword.hex()).replace("0x",""))

file1.close()