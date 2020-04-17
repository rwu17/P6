import unittest

from pathlib import Path
import os
import sys
import math

# Enable importing from src folder
pathToFile = os.getcwd()
path = Path(pathToFile).parent
sys.path.insert(1, str(path))

from parsers.rclParser import rclParsing
from parsers.rcgParser import rcgParsing


class ParseTesting(unittest.TestCase):

    def test_parse_message_01(self):
        print("\nMessage 1: ")
        rcgParser = rcgParsing()
        line = "(msg 0 1 \"(team_graphic_l (16 7 \"8 8 1 1\" \"b c None\" \"bbbbbbbb\" \"bbbbbbbb\" \"bbbbbbbb\" \"bbbbbbbb\" \"bbbbbbbb\" \"bbbbbbbb\" \"bbbbbbbb\" \"bbbbbbbb\")\")"
        rcgParser.strParsing(line)

    def test_init_01(self):
        print("\nInit 1: ")
        rclParser = rclParsing()

        init = "0,3	Recv CYRUS2018_1: (init CYRUS2018 (version 14) (goalie))"
        rclParser.get_initialization_info(init)

    def test_init_02(self):
        print("\nInit 2: ")
        rclParser = rclParsing()

        init = "0,64	Recv CYRUS2018_2: (init CYRUS2018 (version 14))"
        rclParser.get_initialization_info(init)

    def test_init_03(self):
        print("\nInit 3: ")
        rclParser = rclParsing()

        init = "0,374	Recv CYRUS2018_Coach: (init CYRUS2018 (version 14))"
        rclParser.get_initialization_info(init)

    def test_ball_01(self):
        print("\nBall test:")
        rcgParser = rcgParsing()

        frame = "(show 2971 ((b) 29.1118 -1.6618 1.3618 0.8582) ((l 1) 0 0x9 -28.1263 -5.9932 0 0 0.84 1 (v h 180) (s 8000 1 1 55215.8) (f l 4) (c 2 609 2985 2 6 3604 132 94 0 0 1376)) ((l 2) 10 0x1 -0.8798 -2.0675 -0.0069 0.0009 176.717 -90 -1.0828 -1.5506 (v h 120) (s 8000 0.943286 1 28438.1) (f l 4) (c 38 1208 2295 0 2 3543 247 503 0 153 1085)) ((l 3) 4 0x1 0.2307 -20.6194 -0.0001 0.0002 134.143 -90 (v h 120) (s 8000 0.979394 1 26901.7) (f l 2) (c 11 1165 2324 0 2 3512 234 397 1 107 1177)) ((l 4) 5 0x1 -0.1312 15.3931 -0.0272 -0.032 108.846 -90 (v h 120) (s 8000 0.908495 1 36413.9) (f l 11) (c 50 1028 2401 0 2 3481 208 490 0 60 1218)) ((l 5) 13 0x1 15.4659 -13.7535 -0.2537 0.137 151.744 -43 (v h 60) (s 6185.65 0.915218 1 76980.3) (f l 8) (c 26 1381 2041 0 2 3445 226 644 0 99 1160)) ((l 6) 7 0x1 16.6042 -4.376 -0.3043 0.1265 154.912 90 9.8865 -2.2264 (v h 60) (s 7141.18 0.904061 1 6537.69) (f l 11) (c 56 1360 2001 0 2 3419 232 650 0 91 1142)) ((l 7) 9 0x1 20.3602 -23.7404 -0.2518 0.1077 153.309 22 21.0108 -24.7672 (v h 120) (s 5840.76 0.902066 1 68501.2) (f l 2) (c 53 1505 1828 0 2 3388 283 762 0 106 1261)) ((l 8) 6 0x40001 25.4142 4.5755 -0.1725 0.1336 143.501 84 28.0605 -1.9226 (v h 60) (s 6128.93 0.85015 1 12881) (f l 11) (c 82 1527 1730 0 2 3357 241 836 1 74 1230)) ((l 9) 3 0x1 32.6777 -19.7574 -0.1859 0.0077 171.486 -21 38.1908 -28.2654 (v h 60) (s 6507.54 0.983479 1 22016.5) (f l 8) (c 136 1212 1976 0 2 3326 267 639 0 129 1209)) ((l 10) 11 0x1 25.4098 8.0518 -0.1211 0.1707 125.279 90 34.4687 2.2754 (v h 180) (s 6558.48 0.965419 1 13212) (f l 11) (c 38 1304 1951 0 2 3295 240 470 0 150 1267)) ((l 11) 16 0x1 19.9563 -5.7545 -0.1755 0.0936 153.663 82 23.2441 -3.6688 (v h 60) (s 4858.53 0.969346 1 22911.5) (f l 8) (c 60 1438 1764 0 2 3264 236 664 0 112 1121)) ((r 1) 0 0x9 46.6133 -1.4794 -0.0172 -0.012 71.118 90 (v h 60) (s 7648.38 1 1 100999) (f r 2) (c 1 296 3299 1 4 3601 184 177 0 0 2077)) ((r 2) 15 0x1 30.563 -0.8553 -0.0166 0.0002 178.642 90 (v h 60) (s 5842.54 0.879543 1 23991.9) (f r 6) (c 25 1523 1980 0 2 3540 400 525 1 0 1105)) ((r 3) 5 0x1 34.3971 -4.3542 -0.1085 0.1321 93.649 38 (v h 60) (s 7582.14 0.908495 1 26797.5) (f r 2) (c 11 1442 2044 0 2 3509 709 507 1 0 1132)) ((r 4) 4 0x1 38.2848 5.8897 -0.009 0.0237 -126.976 90 (v h 60) (s 8000 0.979394 1 35962.7) (f r 2) (c 7 1216 2253 0 2 3478 481 402 0 0 1351)) ((r 5) 11 0x1 36.6074 -17.5615 -0.0668 -0.0513 -139.929 -1 (v h 60) (s 7551.64 0.965419 1 29012.1) (f r 2) (c 13 1331 2091 0 2 3447 330 456 1 0 1077)) ((r 6) 17 0x1 25.7437 -3.8802 0.0338 0.0214 160.626 45 (v h 60) (s 7800.22 0.801842 1 2802.08) (f r 2) (c 12 1624 1777 0 2 3415 228 642 0 0 976)) ((r 7) 6 0x1 32.1497 8.8456 -0.1078 0.1178 135.636 5 (v h 60) (s 6445.12 0.85015 1 17523) (f r 2) (c 4 1548 1830 0 2 3384 234 437 0 0 1149)) ((r 8) 7 0x1 31.6594 -22.2636 -0.152 -0.0443 -161.091 -52 (v h 120) (s 0 0.504061 0.666 0) (f r 2) (c 18 1598 1735 0 2 3353 221 609 0 0 1052)) ((r 9) 16 0x1 12.0184 25.4303 -0.2071 0.0659 163.702 90 (v h 120) (s 7786.18 0.969346 1 23513.5) (f r 2) (c 15 1601 1697 0 2 3322 197 455 3 28 1449)) ((r 10) 3 0x1 9.3807 -29.4302 -0.2087 0.0426 167.432 -87 (v h 120) (s 7826.93 0.983479 1 9751.87) (f r 6) (c 2 1624 1653 0 2 3291 221 611 1 30 1243)) ((r 11) 10 0x1 4.5062 -1.7835 -0.0653 -0.0003 81.568 -51 (v h 120) (s 7959.28 0.943286 1 11900.9) (f r 7) (c 3 1666 1579 0 2 3260 312 540 1 6 1039)))"
        ball_info = rcgParser.get_ball_info(frame)
        print(ball_info)

    def test_player_01(self):
        rcgParser = rcgParsing()
        line = "(show 82 ((b) 0 0 0 0) ((l 1) 0 0x9 -33.1153 0.2068 0 0 -0.021 0 (v h 120) (s 8000 1 1 129000) (f l 10) (c 0 16 558 0 1 575 2 0 0 0 11)) ((l 2) 10 0x1 -6.0624 -0.2015 0 -0 1.594 -15 (v h 60) (s 8000 0.943286 1 128643) (f l 10) (c 0 20 493 0 1 514 3 9 0 0 7)) ((l 3) 4 0x1 -13.2395 -18.9864 0 -0 55.633 -35 (v h 120) (s 8000 0.979394 1 129400) (f l 10) (c 0 12 470 0 1 483 2 9 0 0 6)) ((l 4) 5 0x1 -13.5681 19.4445 0 0 -55.068 31 (v h 120) (s 8000 0.908495 1 129400) (f l 10) (c 0 12 439 0 1 452 2 8 0 0 9)) ((l 5) 17 0x1 -3.6565 -5.364 0 -0 54.413 -89 (v h 60) (s 8000 0.801842 1 128066) (f l 10) (c 0 26 394 0 1 421 3 8 0 0 6)) ((l 6) 7 0x1 -3.4782 5.1877 0 0 -56.343 90 (v h 60) (s 8000 0.904061 1 128558) (f l 10) (c 0 21 368 0 1 390 2 8 0 0 8)) ((l 7) 15 0x1 -1.8717 -24.4374 0 -0 84.348 -25 (v h 120) (s 8000 0.879543 1 129000) (f l 10) (c 0 16 342 0 1 359 2 8 0 0 8)) ((l 8) 6 0x1 -1.644 24.2617 0 0 -85.67 -15 (v h 120) (s 8000 0.85015 1 129000) (f l 10) (c 0 16 311 0 1 328 2 8 0 0 12)) ((l 9) 3 0x1 -1.6302 -28.2389 0 -0 85.956 -15 (v h 120) (s 8000 0.983479 1 129700) (f l 6) (c 0 9 287 0 1 297 2 8 0 0 68)) ((l 10) 11 0x1 -0.4046 -0.0536 -0 0 -179.824 -90 (v h 60) (s 8000 0.965419 1 130070) (c 0 6 259 0 1 266 3 8 0 0 0)) ((l 11) 16 0x1 -1.1759 -12.6884 0 0 84.478 10 (v h 60) (s 8000 0.969346 1 129661) (f l 10) (c 0 10 224 0 1 235 3 8 0 0 6)) ((r 1) 0 0x9 40.9818 1.0981 -0 0 -88.506 -90 (v h 180) (s 8000 1 1 129802) (f r 11) (c 0 12 559 0 1 572 1 8 0 0 9)) ((r 2) 15 0x1 16.1766 4.7732 -0 -0 -73.725 -90 (v h 60) (s 8000 0.879543 1 129561) (f r 11) (c 0 17 493 0 1 511 3 7 0 0 13)) ((r 3) 5 0x1 16.2411 -3.3866 -0 0 78.121 90 (v h 60) (s 8000 0.908495 1 129645) (f r 11) (c 0 14 465 0 1 480 3 8 0 0 7)) ((r 4) 4 0x1 15.8081 12.9969 -0 -0 -55.302 -90 (v h 120) (s 8000 0.979394 1 129565) (f r 11) (c 0 15 433 0 1 449 2 8 0 0 9)) ((r 5) 11 0x1 16.0799 -14.9927 -0 0 46.755 90 (v h 120) (s 8000 0.965419 1 129734) (f r 11) (c 0 12 405 0 1 418 2 8 0 0 7)) ((r 6) 17 0x1 10.125 0 0 0 -90.387 -90 (v h 60) (s 8000 0.801842 1 130600) (f r 11) (c 0 0 385 0 1 386 3 7 0 0 15)) ((r 7) 6 0x1 10.8481 9.1235 -0 -0 -49.726 -90 (v h 60) (s 8000 0.85015 1 130114) (f r 11) (c 0 8 346 0 1 355 3 7 0 0 14)) ((r 8) 7 0x1 10.8255 -9.4646 0 0 49.009 90 (v h 60) (s 8000 0.904061 1 130036) (f r 11) (c 0 8 315 0 1 324 3 7 0 0 8)) ((r 9) 16 0x1 6.6687 22.0487 0 -0 -17.239 -90 (v h 120) (s 8000 0.969346 1 130200) (f r 11) (c 0 4 288 0 1 293 2 7 0 0 15)) ((r 10) 3 0x1 6.1831 -21.9342 -0 0 15.364 90 (v h 120) (s 8000 0.983479 1 130200) (f r 11) (c 0 4 257 0 1 262 2 7 0 0 5)) ((r 11) 10 0x1 8.5269 -4.4188 -0 -0 62.533 90 (v h 60) (s 8000 0.943286 1 129957) (f r 6) (c 0 10 220 0 1 231 2 7 0 0 23)))"

        player_info = rcgParser.get_player_info(line)

        for x in range(1, 23):
            print(player_info[str(x)]["pos_x"])

    def test_ball_statistics_01(self):
        rcgParser = rcgParsing()
        lines = [
            "(show 82 ((b) 1 0 0 0) ((l 1) 0 0x9 -33.1153 0.2068 0 0 -0.021 0 (v h 120) (s 8000 1 1 129000) (f l 10) (c 0 16 558 0 1 575 2 0 0 0 11)) ((l 2) 10 0x1 -6.0624 -0.2015 0 -0 1.594 -15 (v h 60) (s 8000 0.943286 1 128643) (f l 10) (c 0 20 493 0 1 514 3 9 0 0 7)) ((l 3) 4 0x1 -13.2395 -18.9864 0 -0 55.633 -35 (v h 120) (s 8000 0.979394 1 129400) (f l 10) (c 0 12 470 0 1 483 2 9 0 0 6)) ((l 4) 5 0x1 -13.5681 19.4445 0 0 -55.068 31 (v h 120) (s 8000 0.908495 1 129400) (f l 10) (c 0 12 439 0 1 452 2 8 0 0 9)) ((l 5) 17 0x1 -3.6565 -5.364 0 -0 54.413 -89 (v h 60) (s 8000 0.801842 1 128066) (f l 10) (c 0 26 394 0 1 421 3 8 0 0 6)) ((l 6) 7 0x1 -3.4782 5.1877 0 0 -56.343 90 (v h 60) (s 8000 0.904061 1 128558) (f l 10) (c 0 21 368 0 1 390 2 8 0 0 8)) ((l 7) 15 0x1 -1.8717 -24.4374 0 -0 84.348 -25 (v h 120) (s 8000 0.879543 1 129000) (f l 10) (c 0 16 342 0 1 359 2 8 0 0 8)) ((l 8) 6 0x1 -1.644 24.2617 0 0 -85.67 -15 (v h 120) (s 8000 0.85015 1 129000) (f l 10) (c 0 16 311 0 1 328 2 8 0 0 12)) ((l 9) 3 0x1 -1.6302 -28.2389 0 -0 85.956 -15 (v h 120) (s 8000 0.983479 1 129700) (f l 6) (c 0 9 287 0 1 297 2 8 0 0 68)) ((l 10) 11 0x1 -0.4046 -0.0536 -0 0 -179.824 -90 (v h 60) (s 8000 0.965419 1 130070) (c 0 6 259 0 1 266 3 8 0 0 0)) ((l 11) 16 0x1 -1.1759 -12.6884 0 0 84.478 10 (v h 60) (s 8000 0.969346 1 129661) (f l 10) (c 0 10 224 0 1 235 3 8 0 0 6)) ((r 1) 0 0x9 40.9818 1.0981 -0 0 -88.506 -90 (v h 180) (s 8000 1 1 129802) (f r 11) (c 0 12 559 0 1 572 1 8 0 0 9)) ((r 2) 15 0x1 16.1766 4.7732 -0 -0 -73.725 -90 (v h 60) (s 8000 0.879543 1 129561) (f r 11) (c 0 17 493 0 1 511 3 7 0 0 13)) ((r 3) 5 0x1 16.2411 -3.3866 -0 0 78.121 90 (v h 60) (s 8000 0.908495 1 129645) (f r 11) (c 0 14 465 0 1 480 3 8 0 0 7)) ((r 4) 4 0x1 15.8081 12.9969 -0 -0 -55.302 -90 (v h 120) (s 8000 0.979394 1 129565) (f r 11) (c 0 15 433 0 1 449 2 8 0 0 9)) ((r 5) 11 0x1 16.0799 -14.9927 -0 0 46.755 90 (v h 120) (s 8000 0.965419 1 129734) (f r 11) (c 0 12 405 0 1 418 2 8 0 0 7)) ((r 6) 17 0x1 10.125 0 0 0 -90.387 -90 (v h 60) (s 8000 0.801842 1 130600) (f r 11) (c 0 0 385 0 1 386 3 7 0 0 15)) ((r 7) 6 0x1 10.8481 9.1235 -0 -0 -49.726 -90 (v h 60) (s 8000 0.85015 1 130114) (f r 11) (c 0 8 346 0 1 355 3 7 0 0 14)) ((r 8) 7 0x1 10.8255 -9.4646 0 0 49.009 90 (v h 60) (s 8000 0.904061 1 130036) (f r 11) (c 0 8 315 0 1 324 3 7 0 0 8)) ((r 9) 16 0x1 6.6687 22.0487 0 -0 -17.239 -90 (v h 120) (s 8000 0.969346 1 130200) (f r 11) (c 0 4 288 0 1 293 2 7 0 0 15)) ((r 10) 3 0x1 6.1831 -21.9342 -0 0 15.364 90 (v h 120) (s 8000 0.983479 1 130200) (f r 11) (c 0 4 257 0 1 262 2 7 0 0 5)) ((r 11) 10 0x1 8.5269 -4.4188 -0 -0 62.533 90 (v h 60) (s 8000 0.943286 1 129957) (f r 6) (c 0 10 220 0 1 231 2 7 0 0 23)))",
            "(show 82 ((b) 2 0 0 0) ((l 1) 0 0x9 -33.1153 0.2068 0 0 -0.021 0 (v h 120) (s 8000 1 1 129000) (f l 10) (c 0 16 558 0 1 575 2 0 0 0 11)) ((l 2) 10 0x1 -6.0624 -0.2015 0 -0 1.594 -15 (v h 60) (s 8000 0.943286 1 128643) (f l 10) (c 0 20 493 0 1 514 3 9 0 0 7)) ((l 3) 4 0x1 -13.2395 -18.9864 0 -0 55.633 -35 (v h 120) (s 8000 0.979394 1 129400) (f l 10) (c 0 12 470 0 1 483 2 9 0 0 6)) ((l 4) 5 0x1 -13.5681 19.4445 0 0 -55.068 31 (v h 120) (s 8000 0.908495 1 129400) (f l 10) (c 0 12 439 0 1 452 2 8 0 0 9)) ((l 5) 17 0x1 -3.6565 -5.364 0 -0 54.413 -89 (v h 60) (s 8000 0.801842 1 128066) (f l 10) (c 0 26 394 0 1 421 3 8 0 0 6)) ((l 6) 7 0x1 -3.4782 5.1877 0 0 -56.343 90 (v h 60) (s 8000 0.904061 1 128558) (f l 10) (c 0 21 368 0 1 390 2 8 0 0 8)) ((l 7) 15 0x1 -1.8717 -24.4374 0 -0 84.348 -25 (v h 120) (s 8000 0.879543 1 129000) (f l 10) (c 0 16 342 0 1 359 2 8 0 0 8)) ((l 8) 6 0x1 -1.644 24.2617 0 0 -85.67 -15 (v h 120) (s 8000 0.85015 1 129000) (f l 10) (c 0 16 311 0 1 328 2 8 0 0 12)) ((l 9) 3 0x1 -1.6302 -28.2389 0 -0 85.956 -15 (v h 120) (s 8000 0.983479 1 129700) (f l 6) (c 0 9 287 0 1 297 2 8 0 0 68)) ((l 10) 11 0x1 -0.4046 -0.0536 -0 0 -179.824 -90 (v h 60) (s 8000 0.965419 1 130070) (c 0 6 259 0 1 266 3 8 0 0 0)) ((l 11) 16 0x1 -1.1759 -12.6884 0 0 84.478 10 (v h 60) (s 8000 0.969346 1 129661) (f l 10) (c 0 10 224 0 1 235 3 8 0 0 6)) ((r 1) 0 0x9 40.9818 1.0981 -0 0 -88.506 -90 (v h 180) (s 8000 1 1 129802) (f r 11) (c 0 12 559 0 1 572 1 8 0 0 9)) ((r 2) 15 0x1 16.1766 4.7732 -0 -0 -73.725 -90 (v h 60) (s 8000 0.879543 1 129561) (f r 11) (c 0 17 493 0 1 511 3 7 0 0 13)) ((r 3) 5 0x1 16.2411 -3.3866 -0 0 78.121 90 (v h 60) (s 8000 0.908495 1 129645) (f r 11) (c 0 14 465 0 1 480 3 8 0 0 7)) ((r 4) 4 0x1 15.8081 12.9969 -0 -0 -55.302 -90 (v h 120) (s 8000 0.979394 1 129565) (f r 11) (c 0 15 433 0 1 449 2 8 0 0 9)) ((r 5) 11 0x1 16.0799 -14.9927 -0 0 46.755 90 (v h 120) (s 8000 0.965419 1 129734) (f r 11) (c 0 12 405 0 1 418 2 8 0 0 7)) ((r 6) 17 0x1 10.125 0 0 0 -90.387 -90 (v h 60) (s 8000 0.801842 1 130600) (f r 11) (c 0 0 385 0 1 386 3 7 0 0 15)) ((r 7) 6 0x1 10.8481 9.1235 -0 -0 -49.726 -90 (v h 60) (s 8000 0.85015 1 130114) (f r 11) (c 0 8 346 0 1 355 3 7 0 0 14)) ((r 8) 7 0x1 10.8255 -9.4646 0 0 49.009 90 (v h 60) (s 8000 0.904061 1 130036) (f r 11) (c 0 8 315 0 1 324 3 7 0 0 8)) ((r 9) 16 0x1 6.6687 22.0487 0 -0 -17.239 -90 (v h 120) (s 8000 0.969346 1 130200) (f r 11) (c 0 4 288 0 1 293 2 7 0 0 15)) ((r 10) 3 0x1 6.1831 -21.9342 -0 0 15.364 90 (v h 120) (s 8000 0.983479 1 130200) (f r 11) (c 0 4 257 0 1 262 2 7 0 0 5)) ((r 11) 10 0x1 8.5269 -4.4188 -0 -0 62.533 90 (v h 60) (s 8000 0.943286 1 129957) (f r 6) (c 0 10 220 0 1 231 2 7 0 0 23)))",
            "(show 82 ((b) 3 0 0 0) ((l 1) 0 0x9 -33.1153 0.2068 0 0 -0.021 0 (v h 120) (s 8000 1 1 129000) (f l 10) (c 0 16 558 0 1 575 2 0 0 0 11)) ((l 2) 10 0x1 -6.0624 -0.2015 0 -0 1.594 -15 (v h 60) (s 8000 0.943286 1 128643) (f l 10) (c 0 20 493 0 1 514 3 9 0 0 7)) ((l 3) 4 0x1 -13.2395 -18.9864 0 -0 55.633 -35 (v h 120) (s 8000 0.979394 1 129400) (f l 10) (c 0 12 470 0 1 483 2 9 0 0 6)) ((l 4) 5 0x1 -13.5681 19.4445 0 0 -55.068 31 (v h 120) (s 8000 0.908495 1 129400) (f l 10) (c 0 12 439 0 1 452 2 8 0 0 9)) ((l 5) 17 0x1 -3.6565 -5.364 0 -0 54.413 -89 (v h 60) (s 8000 0.801842 1 128066) (f l 10) (c 0 26 394 0 1 421 3 8 0 0 6)) ((l 6) 7 0x1 -3.4782 5.1877 0 0 -56.343 90 (v h 60) (s 8000 0.904061 1 128558) (f l 10) (c 0 21 368 0 1 390 2 8 0 0 8)) ((l 7) 15 0x1 -1.8717 -24.4374 0 -0 84.348 -25 (v h 120) (s 8000 0.879543 1 129000) (f l 10) (c 0 16 342 0 1 359 2 8 0 0 8)) ((l 8) 6 0x1 -1.644 24.2617 0 0 -85.67 -15 (v h 120) (s 8000 0.85015 1 129000) (f l 10) (c 0 16 311 0 1 328 2 8 0 0 12)) ((l 9) 3 0x1 -1.6302 -28.2389 0 -0 85.956 -15 (v h 120) (s 8000 0.983479 1 129700) (f l 6) (c 0 9 287 0 1 297 2 8 0 0 68)) ((l 10) 11 0x1 -0.4046 -0.0536 -0 0 -179.824 -90 (v h 60) (s 8000 0.965419 1 130070) (c 0 6 259 0 1 266 3 8 0 0 0)) ((l 11) 16 0x1 -1.1759 -12.6884 0 0 84.478 10 (v h 60) (s 8000 0.969346 1 129661) (f l 10) (c 0 10 224 0 1 235 3 8 0 0 6)) ((r 1) 0 0x9 40.9818 1.0981 -0 0 -88.506 -90 (v h 180) (s 8000 1 1 129802) (f r 11) (c 0 12 559 0 1 572 1 8 0 0 9)) ((r 2) 15 0x1 16.1766 4.7732 -0 -0 -73.725 -90 (v h 60) (s 8000 0.879543 1 129561) (f r 11) (c 0 17 493 0 1 511 3 7 0 0 13)) ((r 3) 5 0x1 16.2411 -3.3866 -0 0 78.121 90 (v h 60) (s 8000 0.908495 1 129645) (f r 11) (c 0 14 465 0 1 480 3 8 0 0 7)) ((r 4) 4 0x1 15.8081 12.9969 -0 -0 -55.302 -90 (v h 120) (s 8000 0.979394 1 129565) (f r 11) (c 0 15 433 0 1 449 2 8 0 0 9)) ((r 5) 11 0x1 16.0799 -14.9927 -0 0 46.755 90 (v h 120) (s 8000 0.965419 1 129734) (f r 11) (c 0 12 405 0 1 418 2 8 0 0 7)) ((r 6) 17 0x1 10.125 0 0 0 -90.387 -90 (v h 60) (s 8000 0.801842 1 130600) (f r 11) (c 0 0 385 0 1 386 3 7 0 0 15)) ((r 7) 6 0x1 10.8481 9.1235 -0 -0 -49.726 -90 (v h 60) (s 8000 0.85015 1 130114) (f r 11) (c 0 8 346 0 1 355 3 7 0 0 14)) ((r 8) 7 0x1 10.8255 -9.4646 0 0 49.009 90 (v h 60) (s 8000 0.904061 1 130036) (f r 11) (c 0 8 315 0 1 324 3 7 0 0 8)) ((r 9) 16 0x1 6.6687 22.0487 0 -0 -17.239 -90 (v h 120) (s 8000 0.969346 1 130200) (f r 11) (c 0 4 288 0 1 293 2 7 0 0 15)) ((r 10) 3 0x1 6.1831 -21.9342 -0 0 15.364 90 (v h 120) (s 8000 0.983479 1 130200) (f r 11) (c 0 4 257 0 1 262 2 7 0 0 5)) ((r 11) 10 0x1 8.5269 -4.4188 -0 -0 62.533 90 (v h 60) (s 8000 0.943286 1 129957) (f r 6) (c 0 10 220 0 1 231 2 7 0 0 23)))",
            "(show 82 ((b) -2 0 0 0) ((l 1) 0 0x9 -33.1153 0.2068 0 0 -0.021 0 (v h 120) (s 8000 1 1 129000) (f l 10) (c 0 16 558 0 1 575 2 0 0 0 11)) ((l 2) 10 0x1 -6.0624 -0.2015 0 -0 1.594 -15 (v h 60) (s 8000 0.943286 1 128643) (f l 10) (c 0 20 493 0 1 514 3 9 0 0 7)) ((l 3) 4 0x1 -13.2395 -18.9864 0 -0 55.633 -35 (v h 120) (s 8000 0.979394 1 129400) (f l 10) (c 0 12 470 0 1 483 2 9 0 0 6)) ((l 4) 5 0x1 -13.5681 19.4445 0 0 -55.068 31 (v h 120) (s 8000 0.908495 1 129400) (f l 10) (c 0 12 439 0 1 452 2 8 0 0 9)) ((l 5) 17 0x1 -3.6565 -5.364 0 -0 54.413 -89 (v h 60) (s 8000 0.801842 1 128066) (f l 10) (c 0 26 394 0 1 421 3 8 0 0 6)) ((l 6) 7 0x1 -3.4782 5.1877 0 0 -56.343 90 (v h 60) (s 8000 0.904061 1 128558) (f l 10) (c 0 21 368 0 1 390 2 8 0 0 8)) ((l 7) 15 0x1 -1.8717 -24.4374 0 -0 84.348 -25 (v h 120) (s 8000 0.879543 1 129000) (f l 10) (c 0 16 342 0 1 359 2 8 0 0 8)) ((l 8) 6 0x1 -1.644 24.2617 0 0 -85.67 -15 (v h 120) (s 8000 0.85015 1 129000) (f l 10) (c 0 16 311 0 1 328 2 8 0 0 12)) ((l 9) 3 0x1 -1.6302 -28.2389 0 -0 85.956 -15 (v h 120) (s 8000 0.983479 1 129700) (f l 6) (c 0 9 287 0 1 297 2 8 0 0 68)) ((l 10) 11 0x1 -0.4046 -0.0536 -0 0 -179.824 -90 (v h 60) (s 8000 0.965419 1 130070) (c 0 6 259 0 1 266 3 8 0 0 0)) ((l 11) 16 0x1 -1.1759 -12.6884 0 0 84.478 10 (v h 60) (s 8000 0.969346 1 129661) (f l 10) (c 0 10 224 0 1 235 3 8 0 0 6)) ((r 1) 0 0x9 40.9818 1.0981 -0 0 -88.506 -90 (v h 180) (s 8000 1 1 129802) (f r 11) (c 0 12 559 0 1 572 1 8 0 0 9)) ((r 2) 15 0x1 16.1766 4.7732 -0 -0 -73.725 -90 (v h 60) (s 8000 0.879543 1 129561) (f r 11) (c 0 17 493 0 1 511 3 7 0 0 13)) ((r 3) 5 0x1 16.2411 -3.3866 -0 0 78.121 90 (v h 60) (s 8000 0.908495 1 129645) (f r 11) (c 0 14 465 0 1 480 3 8 0 0 7)) ((r 4) 4 0x1 15.8081 12.9969 -0 -0 -55.302 -90 (v h 120) (s 8000 0.979394 1 129565) (f r 11) (c 0 15 433 0 1 449 2 8 0 0 9)) ((r 5) 11 0x1 16.0799 -14.9927 -0 0 46.755 90 (v h 120) (s 8000 0.965419 1 129734) (f r 11) (c 0 12 405 0 1 418 2 8 0 0 7)) ((r 6) 17 0x1 10.125 0 0 0 -90.387 -90 (v h 60) (s 8000 0.801842 1 130600) (f r 11) (c 0 0 385 0 1 386 3 7 0 0 15)) ((r 7) 6 0x1 10.8481 9.1235 -0 -0 -49.726 -90 (v h 60) (s 8000 0.85015 1 130114) (f r 11) (c 0 8 346 0 1 355 3 7 0 0 14)) ((r 8) 7 0x1 10.8255 -9.4646 0 0 49.009 90 (v h 60) (s 8000 0.904061 1 130036) (f r 11) (c 0 8 315 0 1 324 3 7 0 0 8)) ((r 9) 16 0x1 6.6687 22.0487 0 -0 -17.239 -90 (v h 120) (s 8000 0.969346 1 130200) (f r 11) (c 0 4 288 0 1 293 2 7 0 0 15)) ((r 10) 3 0x1 6.1831 -21.9342 -0 0 15.364 90 (v h 120) (s 8000 0.983479 1 130200) (f r 11) (c 0 4 257 0 1 262 2 7 0 0 5)) ((r 11) 10 0x1 8.5269 -4.4188 -0 -0 62.533 90 (v h 60) (s 8000 0.943286 1 129957) (f r 6) (c 0 10 220 0 1 231 2 7 0 0 23)))",
            "(show 82 ((b) -5 0 0 0) ((l 1) 0 0x9 -33.1153 0.2068 0 0 -0.021 0 (v h 120) (s 8000 1 1 129000) (f l 10) (c 0 16 558 0 1 575 2 0 0 0 11)) ((l 2) 10 0x1 -6.0624 -0.2015 0 -0 1.594 -15 (v h 60) (s 8000 0.943286 1 128643) (f l 10) (c 0 20 493 0 1 514 3 9 0 0 7)) ((l 3) 4 0x1 -13.2395 -18.9864 0 -0 55.633 -35 (v h 120) (s 8000 0.979394 1 129400) (f l 10) (c 0 12 470 0 1 483 2 9 0 0 6)) ((l 4) 5 0x1 -13.5681 19.4445 0 0 -55.068 31 (v h 120) (s 8000 0.908495 1 129400) (f l 10) (c 0 12 439 0 1 452 2 8 0 0 9)) ((l 5) 17 0x1 -3.6565 -5.364 0 -0 54.413 -89 (v h 60) (s 8000 0.801842 1 128066) (f l 10) (c 0 26 394 0 1 421 3 8 0 0 6)) ((l 6) 7 0x1 -3.4782 5.1877 0 0 -56.343 90 (v h 60) (s 8000 0.904061 1 128558) (f l 10) (c 0 21 368 0 1 390 2 8 0 0 8)) ((l 7) 15 0x1 -1.8717 -24.4374 0 -0 84.348 -25 (v h 120) (s 8000 0.879543 1 129000) (f l 10) (c 0 16 342 0 1 359 2 8 0 0 8)) ((l 8) 6 0x1 -1.644 24.2617 0 0 -85.67 -15 (v h 120) (s 8000 0.85015 1 129000) (f l 10) (c 0 16 311 0 1 328 2 8 0 0 12)) ((l 9) 3 0x1 -1.6302 -28.2389 0 -0 85.956 -15 (v h 120) (s 8000 0.983479 1 129700) (f l 6) (c 0 9 287 0 1 297 2 8 0 0 68)) ((l 10) 11 0x1 -0.4046 -0.0536 -0 0 -179.824 -90 (v h 60) (s 8000 0.965419 1 130070) (c 0 6 259 0 1 266 3 8 0 0 0)) ((l 11) 16 0x1 -1.1759 -12.6884 0 0 84.478 10 (v h 60) (s 8000 0.969346 1 129661) (f l 10) (c 0 10 224 0 1 235 3 8 0 0 6)) ((r 1) 0 0x9 40.9818 1.0981 -0 0 -88.506 -90 (v h 180) (s 8000 1 1 129802) (f r 11) (c 0 12 559 0 1 572 1 8 0 0 9)) ((r 2) 15 0x1 16.1766 4.7732 -0 -0 -73.725 -90 (v h 60) (s 8000 0.879543 1 129561) (f r 11) (c 0 17 493 0 1 511 3 7 0 0 13)) ((r 3) 5 0x1 16.2411 -3.3866 -0 0 78.121 90 (v h 60) (s 8000 0.908495 1 129645) (f r 11) (c 0 14 465 0 1 480 3 8 0 0 7)) ((r 4) 4 0x1 15.8081 12.9969 -0 -0 -55.302 -90 (v h 120) (s 8000 0.979394 1 129565) (f r 11) (c 0 15 433 0 1 449 2 8 0 0 9)) ((r 5) 11 0x1 16.0799 -14.9927 -0 0 46.755 90 (v h 120) (s 8000 0.965419 1 129734) (f r 11) (c 0 12 405 0 1 418 2 8 0 0 7)) ((r 6) 17 0x1 10.125 0 0 0 -90.387 -90 (v h 60) (s 8000 0.801842 1 130600) (f r 11) (c 0 0 385 0 1 386 3 7 0 0 15)) ((r 7) 6 0x1 10.8481 9.1235 -0 -0 -49.726 -90 (v h 60) (s 8000 0.85015 1 130114) (f r 11) (c 0 8 346 0 1 355 3 7 0 0 14)) ((r 8) 7 0x1 10.8255 -9.4646 0 0 49.009 90 (v h 60) (s 8000 0.904061 1 130036) (f r 11) (c 0 8 315 0 1 324 3 7 0 0 8)) ((r 9) 16 0x1 6.6687 22.0487 0 -0 -17.239 -90 (v h 120) (s 8000 0.969346 1 130200) (f r 11) (c 0 4 288 0 1 293 2 7 0 0 15)) ((r 10) 3 0x1 6.1831 -21.9342 -0 0 15.364 90 (v h 120) (s 8000 0.983479 1 130200) (f r 11) (c 0 4 257 0 1 262 2 7 0 0 5)) ((r 11) 10 0x1 8.5269 -4.4188 -0 -0 62.533 90 (v h 60) (s 8000 0.943286 1 129957) (f r 6) (c 0 10 220 0 1 231 2 7 0 0 23)))"
        ]

        ball_location_history = []
        for frame in lines:
            ball_info = rcgParser.get_ball_info(frame)
            if float(ball_info["pos_x"]) > 0:
                ball_location_history.append("left")
            elif float(ball_info["pos_x"]) < 0:
                ball_location_history.append("right")

        print("")
        print("Left side: " + str(ball_location_history.count("left") / len(ball_location_history)))
        print("Right side: " + str(ball_location_history.count("right") / len(ball_location_history)))

    def test_ball_statistics_02(self):
        rcgParser = rcgParsing()
        ball_location_history = []
        counter = 1

        with open("test_logfiles/20180621130004-CYRUS2018_0-vs-HELIOS2018_1.rcg", "r") as file:
            line = file.readline()
            
            while line:
                
                # Every 1000 frames, print statistics
                if counter % 1000 == 0:
                    print("")
                    print("Ball percentage for Left side: %.0f%%" 
                        % float((ball_location_history.count("left") / len(ball_location_history) * 100)))
                    print("Ball percentage for Right side: %.0f%%" 
                        % float((ball_location_history.count("right") / len(ball_location_history) * 100)))
                
                if "show" in line:
                    ball_info = rcgParser.get_ball_info(line)
                    if float(ball_info["pos_x"]) > 0:
                        ball_location_history.append("left")
                    elif float(ball_info["pos_x"]) < 0:
                        ball_location_history.append("right")

                line = file.readline()

                counter += 1

    def test_ball_possesion_01(self):
        rcgParser = rcgParsing()
        lines = [
            "(show 82 ((b) 1 0 0 0) ((l 1) 0 0x9 2 0.2068 0 0 -0.021 0 (v h 120) (s 8000 1 1 129000) (f l 10) (c 0 16 558 0 1 575 2 0 0 0 11)) ((l 2) 10 0x1 -6.0624 -0.2015 0 -0 1.594 -15 (v h 60) (s 8000 0.943286 1 128643) (f l 10) (c 0 20 493 0 1 514 3 9 0 0 7)) ((l 3) 4 0x1 -13.2395 -18.9864 0 -0 55.633 -35 (v h 120) (s 8000 0.979394 1 129400) (f l 10) (c 0 12 470 0 1 483 2 9 0 0 6)) ((l 4) 5 0x1 -13.5681 19.4445 0 0 -55.068 31 (v h 120) (s 8000 0.908495 1 129400) (f l 10) (c 0 12 439 0 1 452 2 8 0 0 9)) ((l 5) 17 0x1 -3.6565 -5.364 0 -0 54.413 -89 (v h 60) (s 8000 0.801842 1 128066) (f l 10) (c 0 26 394 0 1 421 3 8 0 0 6)) ((l 6) 7 0x1 -3.4782 5.1877 0 0 -56.343 90 (v h 60) (s 8000 0.904061 1 128558) (f l 10) (c 0 21 368 0 1 390 2 8 0 0 8)) ((l 7) 15 0x1 -1.8717 -24.4374 0 -0 84.348 -25 (v h 120) (s 8000 0.879543 1 129000) (f l 10) (c 0 16 342 0 1 359 2 8 0 0 8)) ((l 8) 6 0x1 -1.644 24.2617 0 0 -85.67 -15 (v h 120) (s 8000 0.85015 1 129000) (f l 10) (c 0 16 311 0 1 328 2 8 0 0 12)) ((l 9) 3 0x1 -1.6302 -28.2389 0 -0 85.956 -15 (v h 120) (s 8000 0.983479 1 129700) (f l 6) (c 0 9 287 0 1 297 2 8 0 0 68)) ((l 10) 11 0x1 -0.4046 -0.0536 -0 0 -179.824 -90 (v h 60) (s 8000 0.965419 1 130070) (c 0 6 259 0 1 266 3 8 0 0 0)) ((l 11) 16 0x1 -1.1759 -12.6884 0 0 84.478 10 (v h 60) (s 8000 0.969346 1 129661) (f l 10) (c 0 10 224 0 1 235 3 8 0 0 6)) ((r 1) 0 0x9 40.9818 1.0981 -0 0 -88.506 -90 (v h 180) (s 8000 1 1 129802) (f r 11) (c 0 12 559 0 1 572 1 8 0 0 9)) ((r 2) 15 0x1 16.1766 4.7732 -0 -0 -73.725 -90 (v h 60) (s 8000 0.879543 1 129561) (f r 11) (c 0 17 493 0 1 511 3 7 0 0 13)) ((r 3) 5 0x1 16.2411 -3.3866 -0 0 78.121 90 (v h 60) (s 8000 0.908495 1 129645) (f r 11) (c 0 14 465 0 1 480 3 8 0 0 7)) ((r 4) 4 0x1 15.8081 12.9969 -0 -0 -55.302 -90 (v h 120) (s 8000 0.979394 1 129565) (f r 11) (c 0 15 433 0 1 449 2 8 0 0 9)) ((r 5) 11 0x1 16.0799 -14.9927 -0 0 46.755 90 (v h 120) (s 8000 0.965419 1 129734) (f r 11) (c 0 12 405 0 1 418 2 8 0 0 7)) ((r 6) 17 0x1 10.125 0 0 0 -90.387 -90 (v h 60) (s 8000 0.801842 1 130600) (f r 11) (c 0 0 385 0 1 386 3 7 0 0 15)) ((r 7) 6 0x1 10.8481 9.1235 -0 -0 -49.726 -90 (v h 60) (s 8000 0.85015 1 130114) (f r 11) (c 0 8 346 0 1 355 3 7 0 0 14)) ((r 8) 7 0x1 10.8255 -9.4646 0 0 49.009 90 (v h 60) (s 8000 0.904061 1 130036) (f r 11) (c 0 8 315 0 1 324 3 7 0 0 8)) ((r 9) 16 0x1 6.6687 22.0487 0 -0 -17.239 -90 (v h 120) (s 8000 0.969346 1 130200) (f r 11) (c 0 4 288 0 1 293 2 7 0 0 15)) ((r 10) 3 0x1 6.1831 -21.9342 -0 0 15.364 90 (v h 120) (s 8000 0.983479 1 130200) (f r 11) (c 0 4 257 0 1 262 2 7 0 0 5)) ((r 11) 10 0x1 8.5269 -4.4188 -0 -0 62.533 90 (v h 60) (s 8000 0.943286 1 129957) (f r 6) (c 0 10 220 0 1 231 2 7 0 0 23)))",
            "(show 82 ((b) 2 0 0 0) ((l 1) 0 0x9 4 0.2068 0 0 -0.021 0 (v h 120) (s 8000 1 1 129000) (f l 10) (c 0 16 558 0 1 575 2 0 0 0 11)) ((l 2) 10 0x1 -6.0624 -0.2015 0 -0 1.594 -15 (v h 60) (s 8000 0.943286 1 128643) (f l 10) (c 0 20 493 0 1 514 3 9 0 0 7)) ((l 3) 4 0x1 -13.2395 -18.9864 0 -0 55.633 -35 (v h 120) (s 8000 0.979394 1 129400) (f l 10) (c 0 12 470 0 1 483 2 9 0 0 6)) ((l 4) 5 0x1 -13.5681 19.4445 0 0 -55.068 31 (v h 120) (s 8000 0.908495 1 129400) (f l 10) (c 0 12 439 0 1 452 2 8 0 0 9)) ((l 5) 17 0x1 -3.6565 -5.364 0 -0 54.413 -89 (v h 60) (s 8000 0.801842 1 128066) (f l 10) (c 0 26 394 0 1 421 3 8 0 0 6)) ((l 6) 7 0x1 -3.4782 5.1877 0 0 -56.343 90 (v h 60) (s 8000 0.904061 1 128558) (f l 10) (c 0 21 368 0 1 390 2 8 0 0 8)) ((l 7) 15 0x1 -1.8717 -24.4374 0 -0 84.348 -25 (v h 120) (s 8000 0.879543 1 129000) (f l 10) (c 0 16 342 0 1 359 2 8 0 0 8)) ((l 8) 6 0x1 -1.644 24.2617 0 0 -85.67 -15 (v h 120) (s 8000 0.85015 1 129000) (f l 10) (c 0 16 311 0 1 328 2 8 0 0 12)) ((l 9) 3 0x1 -1.6302 -28.2389 0 -0 85.956 -15 (v h 120) (s 8000 0.983479 1 129700) (f l 6) (c 0 9 287 0 1 297 2 8 0 0 68)) ((l 10) 11 0x1 -0.4046 -0.0536 -0 0 -179.824 -90 (v h 60) (s 8000 0.965419 1 130070) (c 0 6 259 0 1 266 3 8 0 0 0)) ((l 11) 16 0x1 -1.1759 -12.6884 0 0 84.478 10 (v h 60) (s 8000 0.969346 1 129661) (f l 10) (c 0 10 224 0 1 235 3 8 0 0 6)) ((r 1) 0 0x9 40.9818 1.0981 -0 0 -88.506 -90 (v h 180) (s 8000 1 1 129802) (f r 11) (c 0 12 559 0 1 572 1 8 0 0 9)) ((r 2) 15 0x1 16.1766 4.7732 -0 -0 -73.725 -90 (v h 60) (s 8000 0.879543 1 129561) (f r 11) (c 0 17 493 0 1 511 3 7 0 0 13)) ((r 3) 5 0x1 16.2411 -3.3866 -0 0 78.121 90 (v h 60) (s 8000 0.908495 1 129645) (f r 11) (c 0 14 465 0 1 480 3 8 0 0 7)) ((r 4) 4 0x1 15.8081 12.9969 -0 -0 -55.302 -90 (v h 120) (s 8000 0.979394 1 129565) (f r 11) (c 0 15 433 0 1 449 2 8 0 0 9)) ((r 5) 11 0x1 16.0799 -14.9927 -0 0 46.755 90 (v h 120) (s 8000 0.965419 1 129734) (f r 11) (c 0 12 405 0 1 418 2 8 0 0 7)) ((r 6) 17 0x1 10.125 0 0 0 -90.387 -90 (v h 60) (s 8000 0.801842 1 130600) (f r 11) (c 0 0 385 0 1 386 3 7 0 0 15)) ((r 7) 6 0x1 10.8481 9.1235 -0 -0 -49.726 -90 (v h 60) (s 8000 0.85015 1 130114) (f r 11) (c 0 8 346 0 1 355 3 7 0 0 14)) ((r 8) 7 0x1 10.8255 -9.4646 0 0 49.009 90 (v h 60) (s 8000 0.904061 1 130036) (f r 11) (c 0 8 315 0 1 324 3 7 0 0 8)) ((r 9) 16 0x1 6.6687 22.0487 0 -0 -17.239 -90 (v h 120) (s 8000 0.969346 1 130200) (f r 11) (c 0 4 288 0 1 293 2 7 0 0 15)) ((r 10) 3 0x1 6.1831 -21.9342 -0 0 15.364 90 (v h 120) (s 8000 0.983479 1 130200) (f r 11) (c 0 4 257 0 1 262 2 7 0 0 5)) ((r 11) 10 0x1 8.5269 -4.4188 -0 -0 62.533 90 (v h 60) (s 8000 0.943286 1 129957) (f r 6) (c 0 10 220 0 1 231 2 7 0 0 23)))",
            "(show 82 ((b) 3 0 0 0) ((l 1) 0 0x9 5 0.2068 0 0 -0.021 0 (v h 120) (s 8000 1 1 129000) (f l 10) (c 0 16 558 0 1 575 2 0 0 0 11)) ((l 2) 10 0x1 -6.0624 -0.2015 0 -0 1.594 -15 (v h 60) (s 8000 0.943286 1 128643) (f l 10) (c 0 20 493 0 1 514 3 9 0 0 7)) ((l 3) 4 0x1 -13.2395 -18.9864 0 -0 55.633 -35 (v h 120) (s 8000 0.979394 1 129400) (f l 10) (c 0 12 470 0 1 483 2 9 0 0 6)) ((l 4) 5 0x1 -13.5681 19.4445 0 0 -55.068 31 (v h 120) (s 8000 0.908495 1 129400) (f l 10) (c 0 12 439 0 1 452 2 8 0 0 9)) ((l 5) 17 0x1 -3.6565 -5.364 0 -0 54.413 -89 (v h 60) (s 8000 0.801842 1 128066) (f l 10) (c 0 26 394 0 1 421 3 8 0 0 6)) ((l 6) 7 0x1 -3.4782 5.1877 0 0 -56.343 90 (v h 60) (s 8000 0.904061 1 128558) (f l 10) (c 0 21 368 0 1 390 2 8 0 0 8)) ((l 7) 15 0x1 -1.8717 -24.4374 0 -0 84.348 -25 (v h 120) (s 8000 0.879543 1 129000) (f l 10) (c 0 16 342 0 1 359 2 8 0 0 8)) ((l 8) 6 0x1 -1.644 24.2617 0 0 -85.67 -15 (v h 120) (s 8000 0.85015 1 129000) (f l 10) (c 0 16 311 0 1 328 2 8 0 0 12)) ((l 9) 3 0x1 -1.6302 -28.2389 0 -0 85.956 -15 (v h 120) (s 8000 0.983479 1 129700) (f l 6) (c 0 9 287 0 1 297 2 8 0 0 68)) ((l 10) 11 0x1 -0.4046 -0.0536 -0 0 -179.824 -90 (v h 60) (s 8000 0.965419 1 130070) (c 0 6 259 0 1 266 3 8 0 0 0)) ((l 11) 16 0x1 -1.1759 -12.6884 0 0 84.478 10 (v h 60) (s 8000 0.969346 1 129661) (f l 10) (c 0 10 224 0 1 235 3 8 0 0 6)) ((r 1) 0 0x9 40.9818 1.0981 -0 0 -88.506 -90 (v h 180) (s 8000 1 1 129802) (f r 11) (c 0 12 559 0 1 572 1 8 0 0 9)) ((r 2) 15 0x1 16.1766 4.7732 -0 -0 -73.725 -90 (v h 60) (s 8000 0.879543 1 129561) (f r 11) (c 0 17 493 0 1 511 3 7 0 0 13)) ((r 3) 5 0x1 16.2411 -3.3866 -0 0 78.121 90 (v h 60) (s 8000 0.908495 1 129645) (f r 11) (c 0 14 465 0 1 480 3 8 0 0 7)) ((r 4) 4 0x1 15.8081 12.9969 -0 -0 -55.302 -90 (v h 120) (s 8000 0.979394 1 129565) (f r 11) (c 0 15 433 0 1 449 2 8 0 0 9)) ((r 5) 11 0x1 16.0799 -14.9927 -0 0 46.755 90 (v h 120) (s 8000 0.965419 1 129734) (f r 11) (c 0 12 405 0 1 418 2 8 0 0 7)) ((r 6) 17 0x1 10.125 0 0 0 -90.387 -90 (v h 60) (s 8000 0.801842 1 130600) (f r 11) (c 0 0 385 0 1 386 3 7 0 0 15)) ((r 7) 6 0x1 10.8481 9.1235 -0 -0 -49.726 -90 (v h 60) (s 8000 0.85015 1 130114) (f r 11) (c 0 8 346 0 1 355 3 7 0 0 14)) ((r 8) 7 0x1 10.8255 -9.4646 0 0 49.009 90 (v h 60) (s 8000 0.904061 1 130036) (f r 11) (c 0 8 315 0 1 324 3 7 0 0 8)) ((r 9) 16 0x1 6.6687 22.0487 0 -0 -17.239 -90 (v h 120) (s 8000 0.969346 1 130200) (f r 11) (c 0 4 288 0 1 293 2 7 0 0 15)) ((r 10) 3 0x1 6.1831 -21.9342 -0 0 15.364 90 (v h 120) (s 8000 0.983479 1 130200) (f r 11) (c 0 4 257 0 1 262 2 7 0 0 5)) ((r 11) 10 0x1 8.5269 -4.4188 -0 -0 62.533 90 (v h 60) (s 8000 0.943286 1 129957) (f r 6) (c 0 10 220 0 1 231 2 7 0 0 23)))",
            "(show 82 ((b) -2 0 0 0) ((l 1) 0 0x9 -33.1153 0.2068 0 0 -0.021 0 (v h 120) (s 8000 1 1 129000) (f l 10) (c 0 16 558 0 1 575 2 0 0 0 11)) ((l 2) 10 0x1 -6.0624 -0.2015 0 -0 1.594 -15 (v h 60) (s 8000 0.943286 1 128643) (f l 10) (c 0 20 493 0 1 514 3 9 0 0 7)) ((l 3) 4 0x1 -13.2395 -18.9864 0 -0 55.633 -35 (v h 120) (s 8000 0.979394 1 129400) (f l 10) (c 0 12 470 0 1 483 2 9 0 0 6)) ((l 4) 5 0x1 -13.5681 19.4445 0 0 -55.068 31 (v h 120) (s 8000 0.908495 1 129400) (f l 10) (c 0 12 439 0 1 452 2 8 0 0 9)) ((l 5) 17 0x1 -3.6565 -5.364 0 -0 54.413 -89 (v h 60) (s 8000 0.801842 1 128066) (f l 10) (c 0 26 394 0 1 421 3 8 0 0 6)) ((l 6) 7 0x1 -3.4782 5.1877 0 0 -56.343 90 (v h 60) (s 8000 0.904061 1 128558) (f l 10) (c 0 21 368 0 1 390 2 8 0 0 8)) ((l 7) 15 0x1 -1.8717 -24.4374 0 -0 84.348 -25 (v h 120) (s 8000 0.879543 1 129000) (f l 10) (c 0 16 342 0 1 359 2 8 0 0 8)) ((l 8) 6 0x1 -1.644 24.2617 0 0 -85.67 -15 (v h 120) (s 8000 0.85015 1 129000) (f l 10) (c 0 16 311 0 1 328 2 8 0 0 12)) ((l 9) 3 0x1 -1.6302 -28.2389 0 -0 85.956 -15 (v h 120) (s 8000 0.983479 1 129700) (f l 6) (c 0 9 287 0 1 297 2 8 0 0 68)) ((l 10) 11 0x1 -0.4046 -0.0536 -0 0 -179.824 -90 (v h 60) (s 8000 0.965419 1 130070) (c 0 6 259 0 1 266 3 8 0 0 0)) ((l 11) 16 0x1 -1.1759 -12.6884 0 0 84.478 10 (v h 60) (s 8000 0.969346 1 129661) (f l 10) (c 0 10 224 0 1 235 3 8 0 0 6)) ((r 1) 0 0x9 40.9818 1.0981 -0 0 -88.506 -90 (v h 180) (s 8000 1 1 129802) (f r 11) (c 0 12 559 0 1 572 1 8 0 0 9)) ((r 2) 15 0x1 16.1766 4.7732 -0 -0 -73.725 -90 (v h 60) (s 8000 0.879543 1 129561) (f r 11) (c 0 17 493 0 1 511 3 7 0 0 13)) ((r 3) 5 0x1 16.2411 -3.3866 -0 0 78.121 90 (v h 60) (s 8000 0.908495 1 129645) (f r 11) (c 0 14 465 0 1 480 3 8 0 0 7)) ((r 4) 4 0x1 15.8081 12.9969 -0 -0 -55.302 -90 (v h 120) (s 8000 0.979394 1 129565) (f r 11) (c 0 15 433 0 1 449 2 8 0 0 9)) ((r 5) 11 0x1 16.0799 -14.9927 -0 0 46.755 90 (v h 120) (s 8000 0.965419 1 129734) (f r 11) (c 0 12 405 0 1 418 2 8 0 0 7)) ((r 6) 17 0x1 10.125 0 0 0 -90.387 -90 (v h 60) (s 8000 0.801842 1 130600) (f r 11) (c 0 0 385 0 1 386 3 7 0 0 15)) ((r 7) 6 0x1 10.8481 9.1235 -0 -0 -49.726 -90 (v h 60) (s 8000 0.85015 1 130114) (f r 11) (c 0 8 346 0 1 355 3 7 0 0 14)) ((r 8) 7 0x1 10.8255 -9.4646 0 0 49.009 90 (v h 60) (s 8000 0.904061 1 130036) (f r 11) (c 0 8 315 0 1 324 3 7 0 0 8)) ((r 9) 16 0x1 6.6687 22.0487 0 -0 -17.239 -90 (v h 120) (s 8000 0.969346 1 130200) (f r 11) (c 0 4 288 0 1 293 2 7 0 0 15)) ((r 10) 3 0x1 6.1831 -21.9342 -0 0 15.364 90 (v h 120) (s 8000 0.983479 1 130200) (f r 11) (c 0 4 257 0 1 262 2 7 0 0 5)) ((r 11) 10 0x1 -1 0 -0 -0 62.533 90 (v h 60) (s 8000 0.943286 1 129957) (f r 6) (c 0 10 220 0 1 231 2 7 0 0 23)))",
            "(show 82 ((b) -5 0 0 0) ((l 1) 0 0x9 -33.1153 0.2068 0 0 -0.021 0 (v h 120) (s 8000 1 1 129000) (f l 10) (c 0 16 558 0 1 575 2 0 0 0 11)) ((l 2) 10 0x1 -6.0624 -0.2015 0 -0 1.594 -15 (v h 60) (s 8000 0.943286 1 128643) (f l 10) (c 0 20 493 0 1 514 3 9 0 0 7)) ((l 3) 4 0x1 -13.2395 -18.9864 0 -0 55.633 -35 (v h 120) (s 8000 0.979394 1 129400) (f l 10) (c 0 12 470 0 1 483 2 9 0 0 6)) ((l 4) 5 0x1 -13.5681 19.4445 0 0 -55.068 31 (v h 120) (s 8000 0.908495 1 129400) (f l 10) (c 0 12 439 0 1 452 2 8 0 0 9)) ((l 5) 17 0x1 -3.6565 -5.364 0 -0 54.413 -89 (v h 60) (s 8000 0.801842 1 128066) (f l 10) (c 0 26 394 0 1 421 3 8 0 0 6)) ((l 6) 7 0x1 -3.4782 5.1877 0 0 -56.343 90 (v h 60) (s 8000 0.904061 1 128558) (f l 10) (c 0 21 368 0 1 390 2 8 0 0 8)) ((l 7) 15 0x1 -1.8717 -24.4374 0 -0 84.348 -25 (v h 120) (s 8000 0.879543 1 129000) (f l 10) (c 0 16 342 0 1 359 2 8 0 0 8)) ((l 8) 6 0x1 -1.644 24.2617 0 0 -85.67 -15 (v h 120) (s 8000 0.85015 1 129000) (f l 10) (c 0 16 311 0 1 328 2 8 0 0 12)) ((l 9) 3 0x1 -1.6302 -28.2389 0 -0 85.956 -15 (v h 120) (s 8000 0.983479 1 129700) (f l 6) (c 0 9 287 0 1 297 2 8 0 0 68)) ((l 10) 11 0x1 -0.4046 -0.0536 -0 0 -179.824 -90 (v h 60) (s 8000 0.965419 1 130070) (c 0 6 259 0 1 266 3 8 0 0 0)) ((l 11) 16 0x1 -1.1759 -12.6884 0 0 84.478 10 (v h 60) (s 8000 0.969346 1 129661) (f l 10) (c 0 10 224 0 1 235 3 8 0 0 6)) ((r 1) 0 0x9 40.9818 1.0981 -0 0 -88.506 -90 (v h 180) (s 8000 1 1 129802) (f r 11) (c 0 12 559 0 1 572 1 8 0 0 9)) ((r 2) 15 0x1 16.1766 4.7732 -0 -0 -73.725 -90 (v h 60) (s 8000 0.879543 1 129561) (f r 11) (c 0 17 493 0 1 511 3 7 0 0 13)) ((r 3) 5 0x1 16.2411 -3.3866 -0 0 78.121 90 (v h 60) (s 8000 0.908495 1 129645) (f r 11) (c 0 14 465 0 1 480 3 8 0 0 7)) ((r 4) 4 0x1 15.8081 12.9969 -0 -0 -55.302 -90 (v h 120) (s 8000 0.979394 1 129565) (f r 11) (c 0 15 433 0 1 449 2 8 0 0 9)) ((r 5) 11 0x1 16.0799 -14.9927 -0 0 46.755 90 (v h 120) (s 8000 0.965419 1 129734) (f r 11) (c 0 12 405 0 1 418 2 8 0 0 7)) ((r 6) 17 0x1 10.125 0 0 0 -90.387 -90 (v h 60) (s 8000 0.801842 1 130600) (f r 11) (c 0 0 385 0 1 386 3 7 0 0 15)) ((r 7) 6 0x1 10.8481 9.1235 -0 -0 -49.726 -90 (v h 60) (s 8000 0.85015 1 130114) (f r 11) (c 0 8 346 0 1 355 3 7 0 0 14)) ((r 8) 7 0x1 10.8255 -9.4646 0 0 49.009 90 (v h 60) (s 8000 0.904061 1 130036) (f r 11) (c 0 8 315 0 1 324 3 7 0 0 8)) ((r 9) 16 0x1 6.6687 22.0487 0 -0 -17.239 -90 (v h 120) (s 8000 0.969346 1 130200) (f r 11) (c 0 4 288 0 1 293 2 7 0 0 15)) ((r 10) 3 0x1 6.1831 -21.9342 -0 0 15.364 90 (v h 120) (s 8000 0.983479 1 130200) (f r 11) (c 0 4 257 0 1 262 2 7 0 0 5)) ((r 11) 10 0x1 -4 0 -0 -0 62.533 90 (v h 60) (s 8000 0.943286 1 129957) (f r 6) (c 0 10 220 0 1 231 2 7 0 0 23)))"
        ]

        t1_ball_possesion = []
        t2_ball_possesion = []

        for line in lines:
            player_info = rcgParser.get_player_info(line)
            ball_info = rcgParser.get_ball_info(line)

            closest_distance = 6
            player_possesing = None

            # If the ball is not in the starting position
            if float(ball_info["pos_x"]) != 0 and float(ball_info["pos_y"]) != 0:

                # Find out which player is possesing the ball, if any
                for x in range(1, 23):
                    # Distance from player to ball
                    distance = math.sqrt(pow((float(player_info[str(x)]["pos_x"]) - float(ball_info["pos_x"])), 2) + pow((float(player_info[str(x)]["pos_y"]) - float(ball_info["pos_y"])), 2))
                    
                    # If a player is within 5 units of the ball and closer than any other
                    if distance <= 5 and distance < closest_distance: 
                        closest_distance = distance
                        player_possesing = x
        
            # Save who possesed the ball
            if player_possesing is not None:
                # If the player possesing the ball is from team 1
                if player_possesing <= 11:
                    t1_ball_possesion.append("team1")
                elif player_possesing > 11:
                    t2_ball_possesion.append("team2")

        # Calculate the possesion statistics
        t1_ball_possesion_size = len(t1_ball_possesion)
        t2_ball_possesion_size = len(t2_ball_possesion)

        # Make sure not to divide by zero
        if t1_ball_possesion_size != 0 or t2_ball_possesion_size != 0:
            print("Team 1 ball possesion: %.2f%%" % (float(t1_ball_possesion_size / (t1_ball_possesion_size + t2_ball_possesion_size)) * 100))
            print("Team 2 ball possesion: %.2f%%" % (float(t2_ball_possesion_size / (t1_ball_possesion_size + t2_ball_possesion_size)) * 100))
        

if __name__ == "__main__":
    unittest.main()
