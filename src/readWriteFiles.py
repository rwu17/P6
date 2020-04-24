from threading import Thread
from parsers.rclParser import rclParsing
from parsers.rcgParser import rcgParsing
from pyparsing import ParseException
import os
from math import sqrt

class ReadWriteLogFiles:
    # .rcg variables
    t1_ball_possesion = []
    t2_ball_possesion = []
    ball_location_history = []


    # parsers
    rcgParser = rcgParsing()
    rclParser = rclParsing()

    def multiThreadRWFiles(self, rcg_file, rcl_file):
        self.rcg_file = rcg_file
        self.rcl_file = rcl_file

        Thread(target = self.readLogFileRCL).start()
        Thread(target = self.readLogFileRCG).start()
        

        while self.rcgParser.current_frame != self.rclParser.current_frame:
            if self.rcgParser.current_frame > self.rclParser.current_frame:
                print("rcg is too fast")
            elif self.rcgParser.current_frame < self.rclParser.current_frame:
                print("rcl is too fast")
        


    def readLogFileRCG(self):
        with open("logfiles/" + self.rcg_file, "r") as file:
            counter = 0
            line = file.readline()

            while True:

                if self.rcgParser.is_game_end == True:
                    break
                else:
                    try:
                        '''
                        while int(self.rcgParser.current_frame) != int(self.rclParser.current_frame):
                            if int(self.rcgParser.current_frame) > int(self.rclParser.current_frame):
                                print("rcg is too fast, rcg frame: " + self.rcgParser.current_frame + " rcl frame: " + self.rclParser.current_frame)
                            else:
                                break
                        '''

                        counter += 1
                        self.rcgParser.strParsing(line)

                        # If it is a frame save the location of the ball
                        if "show" in line:
                            ball_info = self.rcgParser.get_ball_info(line)
                            player_info = self.rcgParser.get_player_info(line)
                            
                            self.ball_possesion_statistics(ball_info, player_info)
                            '''
                            player_Ball = str(self.get_player_number_possesing_ball(ball_info, player_info))
                            print("Frame: " + self.rcgParser.current_frame + "  " + player_Ball + " has the ball!")
                            '''
                            # Find out whether the ball is on the left or right side of the playing field
                            if float(ball_info["pos_x"]) > 0:
                                self.ball_location_history.append("left")
                            elif float(ball_info["pos_x"]) < 0:
                                self.ball_location_history.append("right")
                        
                        # Every 1000 frames, print statistics
                        if counter % 100 == 0:
                            self.print_ball_possesion_statistics()
                            self.print_ball_location_statistics()
                        
                    except ParseException as e:
                        print(e)
                        break

                    line = file.readline()
        
            print("Lines parsed: " + str(counter))
            error_line = line if line else "No errors while parsing rcg file"
            print(error_line) 


    def readLogFileRCL(self):
        with open("logfiles/" + self.rcl_file, "r") as file:
            counter = 0
            line = file.readline()

            while True:
                if self.rclParser.is_game_end == True:
                    break
                else:
                    try:
                        '''
                        while int(self.rcgParser.current_frame) != int(self.rclParser.current_frame):
                            if int(self.rcgParser.current_frame) < int(self.rclParser.current_frame):
                                print("rcl is too fast, rcl frame: " + self.rclParser.current_frame + " rcg frame: " + self.rcgParser.current_frame)
                            else:
                                break
                        '''
                                
                        counter += 1
                        self.rclParser.strParsing(line)

                    except ParseException as e:
                        print(e)
                        break

                    line = file.readline()
        
            print("Lines parsed: " + str(counter))
            error_line = line if line else "No errors while parsing rcl file"
            print(error_line) 


    def print_ball_location_statistics(self):
        ball_location_history_size = len(self.ball_location_history)

        # Make sure not to divide by 0
        if ball_location_history_size != 0:

            print("Ball on Left side of field percentage: %.0f%%" 
                % float((self.ball_location_history.count("left") / len(self.ball_location_history) * 100)))
            print("Ball on Right side of field percentage: %.0f%%" 
                % float((self.ball_location_history.count("right") / len(self.ball_location_history) * 100)))
            print("")


    def print_ball_possesion_statistics(self):
        # Calculate the possesion statistics
        t1_ball_possesion_size = len(self.t1_ball_possesion)
        t2_ball_possesion_size = len(self.t2_ball_possesion)

        # Make sure not to divide by zero
        if t1_ball_possesion_size != 0 or t2_ball_possesion_size != 0:
            print("Team 1 ball possesion percentage: %.2f%%" % (float(t1_ball_possesion_size / (t1_ball_possesion_size + t2_ball_possesion_size)) * 100))
            print("Team 2 ball possesion percentage: %.2f%%" % (float(t2_ball_possesion_size / (t1_ball_possesion_size + t2_ball_possesion_size)) * 100))
            print("")


    def ball_possesion_statistics(self, ball_info, player_info):
        player_possesing = self.get_player_number_possesing_ball(ball_info, player_info)
        
        # Save who possesed the ball
        if player_possesing is not None:

            # If the player possesing the ball is from team 1
            if player_possesing <= 11:
                self.t1_ball_possesion.append("team1")
            elif player_possesing > 11:
                self.t2_ball_possesion.append("team2")


    def get_player_number_possesing_ball(self, ball_info, player_info):
        closest_distance = 3
        player_possesing = None

        # If the ball is not in the starting position
        if float(ball_info["pos_x"]) != 0 or float(ball_info["pos_y"]) != 0:
            
            # Find out which player is possesing the ball, if any
            for player_number in range(1, 23):
                
                pos_x_player = float(player_info[str(player_number)]["pos_x"])
                pos_y_player = float(player_info[str(player_number)]["pos_y"])

                pos_x_ball = float(ball_info["pos_x"])
                pos_y_ball = float(ball_info["pos_y"])

                pow1 = pow((pos_x_player - pos_x_ball), 2)
                pow2 = pow((pos_y_player - pos_y_ball), 2)

                # Distance from player to ball
                distance = sqrt(pow1 + pow2)
                
                # If a player is within 5 units of the ball and closer than any other
                if distance <= 2 and distance < closest_distance: 
                    closest_distance = distance
                    player_possesing = player_number

        return player_possesing


    def get_distance_from_player_to_team(self, player_number, player_info):
        distance = {}

        # Team 1
        if player_number <= 11:
            for compare_player_number in range(1, 12):

                # If the two players we are comparing are not the same
                if compare_player_number != player_number:

                    pos_x_player = float(player_info[str(player_number)]["pos_x"])
                    pos_y_player = float(player_info[str(player_number)]["pos_y"])

                    pos_x_compare = float(player_info[str(compare_player_number)]["pos_x"])
                    pos_y_compare = float(player_info[str(compare_player_number)]["pos_y"])

                    pow1 = pow(pos_x_player - pos_x_compare, 2)
                    pow2 = pow(pos_y_player - pos_y_compare, 2)

                    distance[compare_player_number] = sqrt(pow1 + pow2)
        # Team 2
        elif player_number > 11:
            for compare_player_number in range(1, 12):

                # If the two players we are comparing are not the same
                if compare_player_number != player_number:

                    pos_x_player = float(player_info[str(player_number)]["pos_x"])
                    pos_y_player = float(player_info[str(player_number)]["pos_y"])

                    pos_x_compare = float(player_info[str(compare_player_number)]["pos_x"])
                    pos_y_compare = float(player_info[str(compare_player_number)]["pos_y"])

                    pow1 = pow(pos_x_player - pos_x_compare, 2)
                    pow2 = pow(pos_y_player - pos_y_compare, 2)

                    distance[compare_player_number] = sqrt(pow1 + pow2)

        return distance
