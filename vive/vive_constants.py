def in_m(i):
    return i * 0.0254

CALIBRATION_TIME = 1000000000

T1_SERIAL = "LHR-CFF88C2E"
T2_SERIAL = "LHR-1E6A3E70"
LH1_SERIAL = "LHB-947E81C8"
LH2_SERIAL = "LHB-A641CC30"
OLD_LH_SERIAL = "LHB-24CD1E0C"

# x = left/right, y = up/down, z = front/back
LH0_REAL_POS = (in_m(-50), in_m(0), in_m(-9))

# around 
LH0_REAL_ANGLE = (0, -75, 0)

T0_SERIAL = T2_SERIAL
LH0_SERIAL = LH1_SERIAL
TEAM_NUMBER = 1111
HZ = 30