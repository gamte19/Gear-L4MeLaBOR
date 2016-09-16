from pong import *
import pygame

def main():
    """ Main Program """

    # Call this function so the Pygame library can initialize itself
    pygame.init()

    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])

    # Set the title of the window
    pygame.display.set_caption('Pong')

    # Create the player paddle object
    player = Player(150, 290)
    player2 = Player(550, 290)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)
    movingsprites.add(player2)

    rooms = []

    room = Room()
    rooms.append(room)

    current_room_no = 0
    current_room = rooms[current_room_no]

    clock = pygame.time.Clock()

    done = False

    while not done:

        # --- Event Processing ---

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)
                # player2
                if event.key == pygame.K_a:
                    player2.changespeed(-5, 0)
                if event.key == pygame.K_d:
                    player2.changespeed(5, 0)
                if event.key == pygame.K_w:
                    player2.changespeed(0, -5)
                if event.key == pygame.K_s:
                    player2.changespeed(0, 5)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)
                # player2
                if event.key == pygame.K_a:
                    player2.changespeed(5, 0)
                if event.key == pygame.K_d:
                    player2.changespeed(-5, 0)
                if event.key == pygame.K_w:
                    player2.changespeed(0, 5)
                if event.key == pygame.K_s:
                    player2.changespeed(0, -5)

        # --- Game Logic ---

        player.move(current_room.wall_list)
        player2.move(current_room.wall_list)

        # --- Drawing ---
        screen.fill(BLACK)

        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
