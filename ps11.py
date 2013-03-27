# Problem Set 11: Simulating robots
# Name: c4nn1b4l

from itertools import product, count
from pylab import plot, show, title, xlabel, ylabel
import math
import random
import ps11_visualize

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).

        x: a real number indicating the x-coordinate
        y: a real number indicating the y-coordinate
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: integer representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)


# === Problems 1 and 2

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        if type(height) != int or height <= 0 or type(width) != int or width <= 0:
            raise ValueError('room size must be > 0, and must be an integer')
        self.width = width
        self.height = height
        self.CleanBlocks = []
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        if (int(pos.getX()), int(pos.getY())) not in self.CleanBlocks:
            self.CleanBlocks.append((int(pos.getX()), int(pos.getY())))
    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        if (m, n) in self.CleanBlocks:
            return True
        else:
            return False
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return len(list(product(list(range(self.width+1))[1:], list(range(self.height+1))[1:])))
    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return len(self.CleanBlocks)
    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        return Position(random.uniform(0, self.width), random.uniform(0, self.height))
    def isPositionInRoom(self, pos):
        """
        Return True if POS is inside the room.

        pos: a Position object.
        returns: True if POS is in the room, False otherwise.
        """
        if pos.getY() > self.height or pos.getX() > self.width or pos.getX() < 0 or pos.getY() < 0:
            return False
        else:
            return True


class BaseRobot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in
    the room.  The robot also has a fixed speed.

    Subclasses of BaseRobot should provide movement strategies by
    implementing updatePositionAndClean(), which simulates a single
    time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified
        room. The robot initially has a random direction d and a
        random position p in the room.

        The direction d is an integer satisfying 0 <= d < 360; it
        specifies an angle in degrees.

        p is a Position object giving the robot's position.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.position = room.getRandomPosition()
        self.direction = random.randrange(359)
    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction
    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position
    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction
    # def __str__(self):
    #     """#for debugging purposes"""
    #     return '<X: %f Y: %f>'%((self.position.getX()),  (self.position.getY()))


class Robot(BaseRobot):
    """
    A Robot is a BaseRobot with the standard movement strategy.

    At each time-step, a Robot attempts to move in its current
    direction; when it hits a wall, it chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        if self.speed < 1:
            possible_path = self.position.getNewPosition(self.direction, self.speed)
            while not self.room.isPositionInRoom(possible_path):
                self.setRobotDirection(random.randrange(359))
                possible_path = self.position.getNewPosition(self.direction, self.speed)
            self.setRobotPosition(possible_path)
            self.room.cleanTileAtPosition(self.position)
        else:
            possible_moves_on_one_clock = int(self.speed)
            for i in range(possible_moves_on_one_clock):
                possible_path = self.position.getNewPosition(self.direction, 1)
                while not self.room.isPositionInRoom(possible_path):
                    self.setRobotDirection(random.randrange(359))
                    possible_path = self.position.getNewPosition(self.direction, 1)
                self.setRobotPosition(possible_path)
                self.room.cleanTileAtPosition(self.position)
            possible_path = self.position.getNewPosition(self.direction, (self.speed - possible_moves_on_one_clock))
            while not self.room.isPositionInRoom(possible_path):
                self.setRobotDirection(random.randrange(359))
                possible_path = self.position.getNewPosition(self.direction, (self.speed - possible_moves_on_one_clock))
            self.setRobotPosition(possible_path)
            self.room.cleanTileAtPosition(self.position)



# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type, visualize):
    """
    Runs NUM_TRIALS trials of the simulation and returns a list of
    lists, one per trial. The list for a trial has an element for each
    timestep of that trial, the value of which is the percentage of
    the room that is clean after that timestep. Each trial stops when
    MIN_COVERAGE of the room is clean.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE,
    each with speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    Visualization is turned on when boolean VISUALIZE is set to True.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    visualize: a boolean (True to turn on visualization)
    """
    #initialization of variables
    list_of_results = []
    
    #trial loop
    for i in range(num_trials):
        list_of_results.append(singleSimulation(num_robots, speed, width, height, min_coverage, robot_type, visualize))
    return list_of_results


def singleSimulation(num_robots, speed, width, height, min_coverage, robot_type, visualize):
    dict_of_robots = {}
    sing_result = []
    rectroom = RectangularRoom(width, height)
    if visualize:
        anim= ps11_visualize.RobotVisualization(num_robots,width, height)
    for u in range(num_robots):
            dict_of_robots[u] = robot_type(rectroom, speed)
    while (rectroom.getNumCleanedTiles() / rectroom.getNumTiles()) < min_coverage:
        for robi in dict_of_robots.keys():
            if visualize:
                anim.update(rectroom, dict_of_robots.values()) 
            dict_of_robots[robi].updatePositionAndClean()
            if (rectroom.getNumCleanedTiles() / rectroom.getNumTiles()) >= min_coverage:
                return sing_result
        sing_result.append((rectroom.getNumCleanedTiles() / rectroom.getNumTiles()))
    if visualize:
        anim.done()
    return sing_result


# === Provided function
def computeMeans(list_of_lists):
    """
    Returns a list as long as the longest list in LIST_OF_LISTS, where
    the value at index i is the average of the values at index i in
    all of LIST_OF_LISTS' lists.

    Lists shorter than the longest list are padded with their final
    value to be the same length.
    """
    # Find length of longest list
    longest = 0
    for lst in list_of_lists:
        if len(lst) > longest:
           longest = len(lst)
    # Get totals
    tots = [0]*(longest)
    for lst in list_of_lists:
        for i in range(longest):
            if i < len(lst):
                tots[i] += lst[i]
            else:
                tots[i] += lst[-1]
    # Convert tots to an array to make averaging across each index easier
    tots = pylab.array(tots)
    # Compute means
    means = tots/float(len(list_of_lists))
    return means


# === Problem 4
def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on room size.
    """

    interested_in = list(range(5,30,5))
    proc_sim_data = []
    for item in interested_in:
        len_sim_data = []
        raw_sim_data = runSimulation(1, 1.0, item, item, 0.75, 100, Robot, False)
        for mes in raw_sim_data:
            len_sim_data.append(len(mes))
        proc_sim_data.append(sum(len_sim_data)/len(len_sim_data))
    plot(interested_in, proc_sim_data)
    title('Dependence of cleaning time on room size')
    xlabel('area of the room (tiles)')
    ylabel('mean time (clocks)')
    show()


def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    interested_in = list(range(1,10))
    proc_sim_data = []
    for item in interested_in:
        len_sim_data = []
        raw_sim_data = runSimulation(item, 1.0, 25, 25, 0.75, 100, Robot, False)
        for mes in raw_sim_data:
            len_sim_data.append(len(mes))
        proc_sim_data.append(sum(len_sim_data)/len(len_sim_data))
    plot(interested_in, proc_sim_data)
    title('Dependence of cleaning time on number of robots')
    xlabel('number of robots (tiles)')
    ylabel('mean time (clocks)')
    show()


def showPlot3():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    interested_in = [(20,20),(25,16),(40,10),(50,8),(80,5),(100,4)]
    proc_sim_data = []
    for item in interested_in:
        len_sim_data = []
        raw_sim_data = runSimulation(2, 1.0, item[0], item[1], 0.75, 100, Robot, False)
        for mes in raw_sim_data:
            len_sim_data.append(len(mes))
        proc_sim_data.append(sum(len_sim_data)/len(len_sim_data))
    plot([1,1.56,4,6.25,16,25], proc_sim_data)
    title('Dependence of cleaning time on room shape')
    xlabel('ratio of width to height')
    ylabel('mean time (clocks)')
    show()


def showPlot4():
    """
    Produces a plot showing cleaning time vs. percentage cleaned, for
    each of 1-5 robots.
    """
    overall_data = []
    per_to_clean = [round(x * 0.1,1) for x in range(0,10)]
    number_of_robots = list(range(1,6))
    for per in per_to_clean:
        proc_sim_data = []
        for item in number_of_robots:
            len_sim_data = []
            raw_sim_data = runSimulation(item, 1.0, 25, 25, per, 10, Robot, False)
            for mes in raw_sim_data:
                len_sim_data.append(len(mes))
            proc_sim_data.append(sum(len_sim_data)/len(len_sim_data))
        overall_data.append(proc_sim_data)
    plot(per_to_clean, overall_data)
    title('cleaning time vs. percentage cleaned')
    xlabel('percentage clean')
    ylabel('mean time (clocks)')
    show()


# === Problem 5

class RandomWalkRobot(BaseRobot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement
    strategy: it chooses a new direction at random after each
    time-step.
    """
    def updatePositionAndClean(self):
        if self.speed < 1:
                possible_path = self.position.getNewPosition(random.randrange(359), self.speed)
                while not self.room.isPositionInRoom(possible_path):
                    self.setRobotDirection(random.randrange(359))
                    possible_path = self.position.getNewPosition(self.direction, self.speed)
                self.setRobotPosition(possible_path)
                self.room.cleanTileAtPosition(self.position)
        else:
            possible_moves_on_one_clock = int(self.speed)
            for i in range(possible_moves_on_one_clock):
                possible_path = self.position.getNewPosition(random.randrange(359), 1)
                while not self.room.isPositionInRoom(possible_path):
                    self.setRobotDirection(random.randrange(359))
                    possible_path = self.position.getNewPosition(self.direction, 1)
                self.setRobotPosition(possible_path)
                self.room.cleanTileAtPosition(self.position)
            possible_path = self.position.getNewPosition(random.randrange(359), (self.speed - possible_moves_on_one_clock))
            while not self.room.isPositionInRoom(possible_path):
                self.setRobotDirection(random.randrange(359))
                possible_path = self.position.getNewPosition(self.direction, (self.speed - possible_moves_on_one_clock))
            self.setRobotPosition(possible_path)
            self.room.cleanTileAtPosition(self.position)


# === Problem 6

def showPlot5():
    """
    Produces a plot comparing the two robot strategies.
    """
    interested_in = list(range(1,10))
    proc_sim_data = []
    for item in interested_in:
        len_sim_data = []
        raw_sim_data = runSimulation(item, 1.0, 25, 25, 0.75, 100, Robot, False)
        len_sim_data2 = []
        raw_sim_data2 = runSimulation(item, 1.0, 25, 25, 0.75, 100, RandomWalkRobot, False)
        for mes in raw_sim_data:
            len_sim_data.append(len(mes))
        for mes in raw_sim_data2:
            len_sim_data2.append(len(mes))
        overa = [sum(len_sim_data)/len(len_sim_data), sum(len_sim_data2)/len(len_sim_data2)]
        proc_sim_data.append(overa)
    plot(interested_in, proc_sim_data)
    title('performance comparision of the two types of bots')
    xlabel('number of robots')
    ylabel('mean time (clocks)')
    show()
