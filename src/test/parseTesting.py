import unittest

from pathlib import Path
import os
import sys

# Enable importing from src folder
pathToFile = os.getcwd()
path = Path(pathToFile).parent
sys.path.insert(1, str(path))

from rclParser import rclParsing
from rcgParser import rcgParsing


class ParseTesting(unittest.TestCase):

    def setUp(self):
        self.rclParser = rclParsing()
        self.rcgParser = rcgParsing()

    def test_init_01(self):
        init = "0,3	Recv CYRUS2018_1: (init CYRUS2018 (version 14) (goalie))"
        self.rclParser.get_initialization_info(init)

    def test_init_02(self):
        init = "0,64	Recv CYRUS2018_2: (init CYRUS2018 (version 14))"
        self.rclParser.get_initialization_info(init)

    def test_init_03(self):
        init = "0,374	Recv CYRUS2018_Coach: (init CYRUS2018 (version 14))"
        self.rclParser.get_initialization_info(init)

    def test_ball_01(self):
        frame = "(show 2971 ((b) 29.1118 -1.6618 1.3618 0.8582) ((l 1) 0 0x9 -28.1263 -5.9932 0 0 0.84 1 (v h 180) (s 8000 1 1 55215.8) (f l 4) (c 2 609 2985 2 6 3604 132 94 0 0 1376)) ((l 2) 10 0x1 -0.8798 -2.0675 -0.0069 0.0009 176.717 -90 -1.0828 -1.5506 (v h 120) (s 8000 0.943286 1 28438.1) (f l 4) (c 38 1208 2295 0 2 3543 247 503 0 153 1085)) ((l 3) 4 0x1 0.2307 -20.6194 -0.0001 0.0002 134.143 -90 (v h 120) (s 8000 0.979394 1 26901.7) (f l 2) (c 11 1165 2324 0 2 3512 234 397 1 107 1177)) ((l 4) 5 0x1 -0.1312 15.3931 -0.0272 -0.032 108.846 -90 (v h 120) (s 8000 0.908495 1 36413.9) (f l 11) (c 50 1028 2401 0 2 3481 208 490 0 60 1218)) ((l 5) 13 0x1 15.4659 -13.7535 -0.2537 0.137 151.744 -43 (v h 60) (s 6185.65 0.915218 1 76980.3) (f l 8) (c 26 1381 2041 0 2 3445 226 644 0 99 1160)) ((l 6) 7 0x1 16.6042 -4.376 -0.3043 0.1265 154.912 90 9.8865 -2.2264 (v h 60) (s 7141.18 0.904061 1 6537.69) (f l 11) (c 56 1360 2001 0 2 3419 232 650 0 91 1142)) ((l 7) 9 0x1 20.3602 -23.7404 -0.2518 0.1077 153.309 22 21.0108 -24.7672 (v h 120) (s 5840.76 0.902066 1 68501.2) (f l 2) (c 53 1505 1828 0 2 3388 283 762 0 106 1261)) ((l 8) 6 0x40001 25.4142 4.5755 -0.1725 0.1336 143.501 84 28.0605 -1.9226 (v h 60) (s 6128.93 0.85015 1 12881) (f l 11) (c 82 1527 1730 0 2 3357 241 836 1 74 1230)) ((l 9) 3 0x1 32.6777 -19.7574 -0.1859 0.0077 171.486 -21 38.1908 -28.2654 (v h 60) (s 6507.54 0.983479 1 22016.5) (f l 8) (c 136 1212 1976 0 2 3326 267 639 0 129 1209)) ((l 10) 11 0x1 25.4098 8.0518 -0.1211 0.1707 125.279 90 34.4687 2.2754 (v h 180) (s 6558.48 0.965419 1 13212) (f l 11) (c 38 1304 1951 0 2 3295 240 470 0 150 1267)) ((l 11) 16 0x1 19.9563 -5.7545 -0.1755 0.0936 153.663 82 23.2441 -3.6688 (v h 60) (s 4858.53 0.969346 1 22911.5) (f l 8) (c 60 1438 1764 0 2 3264 236 664 0 112 1121)) ((r 1) 0 0x9 46.6133 -1.4794 -0.0172 -0.012 71.118 90 (v h 60) (s 7648.38 1 1 100999) (f r 2) (c 1 296 3299 1 4 3601 184 177 0 0 2077)) ((r 2) 15 0x1 30.563 -0.8553 -0.0166 0.0002 178.642 90 (v h 60) (s 5842.54 0.879543 1 23991.9) (f r 6) (c 25 1523 1980 0 2 3540 400 525 1 0 1105)) ((r 3) 5 0x1 34.3971 -4.3542 -0.1085 0.1321 93.649 38 (v h 60) (s 7582.14 0.908495 1 26797.5) (f r 2) (c 11 1442 2044 0 2 3509 709 507 1 0 1132)) ((r 4) 4 0x1 38.2848 5.8897 -0.009 0.0237 -126.976 90 (v h 60) (s 8000 0.979394 1 35962.7) (f r 2) (c 7 1216 2253 0 2 3478 481 402 0 0 1351)) ((r 5) 11 0x1 36.6074 -17.5615 -0.0668 -0.0513 -139.929 -1 (v h 60) (s 7551.64 0.965419 1 29012.1) (f r 2) (c 13 1331 2091 0 2 3447 330 456 1 0 1077)) ((r 6) 17 0x1 25.7437 -3.8802 0.0338 0.0214 160.626 45 (v h 60) (s 7800.22 0.801842 1 2802.08) (f r 2) (c 12 1624 1777 0 2 3415 228 642 0 0 976)) ((r 7) 6 0x1 32.1497 8.8456 -0.1078 0.1178 135.636 5 (v h 60) (s 6445.12 0.85015 1 17523) (f r 2) (c 4 1548 1830 0 2 3384 234 437 0 0 1149)) ((r 8) 7 0x1 31.6594 -22.2636 -0.152 -0.0443 -161.091 -52 (v h 120) (s 0 0.504061 0.666 0) (f r 2) (c 18 1598 1735 0 2 3353 221 609 0 0 1052)) ((r 9) 16 0x1 12.0184 25.4303 -0.2071 0.0659 163.702 90 (v h 120) (s 7786.18 0.969346 1 23513.5) (f r 2) (c 15 1601 1697 0 2 3322 197 455 3 28 1449)) ((r 10) 3 0x1 9.3807 -29.4302 -0.2087 0.0426 167.432 -87 (v h 120) (s 7826.93 0.983479 1 9751.87) (f r 6) (c 2 1624 1653 0 2 3291 221 611 1 30 1243)) ((r 11) 10 0x1 4.5062 -1.7835 -0.0653 -0.0003 81.568 -51 (v h 120) (s 7959.28 0.943286 1 11900.9) (f r 7) (c 3 1666 1579 0 2 3260 312 540 1 6 1039)))"
        parsed = self.rcgParser.get_ball_info(frame)
        print("Pos1: " + parsed[1][0])
        print("Pos2: " + parsed[1][1])
        print("Pos3: " + parsed[1][2])
        print("Pos4: " + parsed[1][3])


if __name__ == "__main__":
    unittest.main()
