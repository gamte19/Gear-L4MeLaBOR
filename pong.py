import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RESOLUTION_X = 800
RESOLUTION_Y = 600


class Wall(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """

    def __init__(self, x, y, width, height, color):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the
    player controls """

    # Set speed vector
    speed_x = 0
    speed_y = 0

    def __init__(self, x, y, image_x, image_y):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([image_x, image_y])
        self.image.fill(WHITE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def changespeed(self, x, y):
        """ Change the speed of the player. Called with a keypress. """
        self.speed_x += x
        self.speed_y += y

    def move(self, walls):
        """ Find a new position for the player """

        # Move left/right
        self.rect.x += self.speed_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.speed_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.speed_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.speed_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

class Ball(pygame.sprite.Sprite):
    speed_x = 0
    speed_y = -5

    def __init__(self, x, y):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([10, 10])
        self.image.fill(WHITE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def changespeed(self, x, y):
        """ Change the speed of the player. Called with a keypress. """
        self.speed_x += x
        self.speed_y += y

    def move(self, walls):
        """ Find a new position for the player """

        # Move left/right
        self.rect.x += self.speed_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.speed_x > 0:
                self.rect.right = block.rect.left
                self.speed_x = self.speed_x * -1
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
                self.speed_x = self.speed_x * -1

        # Move up/down
        self.rect.y += self.speed_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.speed_y > 0:
                self.rect.bottom = block.rect.top
                self.speed_y = self.speed_y * -1
            else:
                self.rect.top = block.rect.bottom
                self.speed_y = self.speed_y * -1


class Room(object):
    """ Base class for all rooms. """

    # Each room has a list of walls, and of enemy sprites.
    wall_list = pygame.sprite.Group()
    paddle_wall_list = pygame.sprite.Group()

    def __init__(self):
        """ Constructor, create our lists. """

        walls = [[0, 0, 10, 600, WHITE],
                 [790, 0, 10, 600, WHITE],
                 [10, 0, 780, 10, WHITE],
                 [395, 300, 10, 300, WHITE]]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        walls_for_paddles = walls
        walls_for_paddles.append([10, 599, 800, 1, BLACK])
        walls_for_paddles.append([399, 10, 1, 490, BLACK])

        for item in walls_for_paddles:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.paddle_wall_list.add(wall)
