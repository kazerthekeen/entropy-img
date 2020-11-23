import cv2 as cv
import numpy as np

resistance = np.array([81 ,76 ,86 ,57 ,65 ,90 ,48 ,75 ,93 ,17 ,51 ,63 ,94 ,10 ,91 ,49 ,21 ,26 ,82 ,56 ,38 ,15 ,87 ,44 ,88 ,23 ,18 ,67 ,14 ,77 ,13 ,99 ,41 ,32 ,58 ,98 ,19 ,22 ,89 ,53 ,54 ,69 ,50 ,25 ,20 ,31 ,29 ,74 ,96 ,73 ,59 ,52 ,11 ,95 ,61 ,66 ,35 ,68 ,78 ,37 ,71 ,45 ,62 ,83, 100 ,79 ,40 ,16 ,30 ,12 ,80 ,60 ,46 ,84 ,39 ,97 ,36 ,24 ,27 ,55 ,47 ,92 ,43 ,70 ,28 ,64 ,85 ,33 ,34 ,72 ,42])

init_energy = np.array([590, 483, 228, 216, 536, 539, 200, 767, 866, 169, 915, 562, 485, 586, 276, 741, 451, 227, 707, 247, 922, 977, 131, 638, 721, 738, 385, 675, 964, 813, 820,  41, 278, 851,  21, 332, 868, 809, 167, 118, 804, 126, 375, 681, 934, 503, 761, 863, 49, 144, 566,  37, 109, 411, 353, 143, 889, 559, 746, 716, 636, 634, 953, 742, 487, 70, 405, 153, 637,  15, 610, 909,  44, 878, 600, 843, 855,  68,  31, 352, 554, 628, 219, 673, 896, 532, 254, 482, 358, 743,159, ])

def temp(energy, x):
    return energy[x] / resistance[x]

def calculate(length):
    max = len(init_energy)
    energy = init_energy
    img =  []
    for y in range(length):
        t = energy/resistance
        f = energy.copy()
        for x in range(max):
                if x+1 in range(max):
                    f[x] += t[x+1] - t[x]
                if x-1 in range(max):
                    f[x] += t[x-1] - t[x]
        img.append(f/resistance)
        energy = f
    return np.array(img)

def rescale(img):
    m = max(img[0])
    print(m)
    return img/m*255


img = calculate(1000)
img = rescale(img)
print(img)
cv.imwrite("entropy.png", img)
