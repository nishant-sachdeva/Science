N = 108

[lx, ly , lz ]= [ float(18e-10)]*3

min_dist = float(3.4e-10)
sigma = min_dist


avogardo_number = float(6.0221415e23)
epsilon = float(0.238 * 4184 / avogardo_number)
# KCal/mole : Has to be convered to Joule / Atom

number_of_frames = 300

timestep = float(4*1e-15)

# atomic_mass_unit = float(1.66e-24) # in grams

mass = float(40*1.66e-24)

K = float(1.38e-23) 
TEMP = 300 
delta = float(1e-21)

maxwell_scale =  round((K*TEMP/mass )**0.5)
# print(maxwell_scale)