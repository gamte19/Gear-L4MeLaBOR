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
    player = Player(150, 290, 100, 10)
    player2 = Player(550, 290, 100, 10)
    player_90 = Player(player.rect.x, player.rect.y-50, 10, 100)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)
    movingsprites.add(player2)
    ball = Ball(400, 200)
    movingsprites.add(ball)

    room = Room()

    clock = pygame.time.Clock()

    done = False

    switch = [False, None]
    while not done:


        # --- Event Processing ---

        for event in pygame.event.get():
            pygame.key.set_repeat(100, 10)
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)
                # player2
                elif event.key == pygame.K_a:
                    player2.changespeed(-5, 0)
                elif event.key == pygame.K_d:
                    player2.changespeed(5, 0)
                elif event.key == pygame.K_w:
                    player2.changespeed(0, -5)
                elif event.key == pygame.K_s:
                    player2.changespeed(0, 5)
                elif event.key == pygame.K_i:
                    if switch[0] is False:
                        switch[1] = player
                        temp_player = player
                        player = player_90
                        temp_player.kill()
                        switch[0] = True
                        screen.blit(player.image, (100, 100))
                        movingsprites.add(player)

                elif event.key == pygame.K_p:
                    #if switch is True:
                    temp_player = player
                    player = switch[1]
                    switch[1] = player
                    temp_player.kill()
                    switch[0] = False
                    screen.blit(player.image, (100, 100))
                    movingsprites.add(player)
                    pygame.display.update()
                # if event.key == pygame.K_p:
                # if event.key == pygame.K_i:
                #    if event.key == pygame.K_i:
                #        player2.rect.left=550
                #        player2.rect.right=560
                #        player2.rect.top=200
                #        player2.rect.bottom=300

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)
                # player2
                elif event.key == pygame.K_a:
                    player2.changespeed(5, 0)
                elif event.key == pygame.K_d:
                    player2.changespeed(-5, 0)
                elif event.key == pygame.K_w:
                    player2.changespeed(0, 5)
                elif event.key == pygame.K_s:
                    player2.changespeed(0, -5)
                # if event.key == pygame.K_i:
                #    player2.image = pygame.Surface([10, 100])
                #    player2.rect.left-=5
                #    player2.rect.right-=100
                #    player2.rect.top-=100
                #    player2.rect.bottom-=5



        # --- Game Logic ---
        player.move(room.paddle_wall_list)
        player2.move(room.paddle_wall_list)
        ball.move(room.wall_list)


        # --- Drawing ---
        screen.fill(BLACK)

        movingsprites.draw(screen)
        room.wall_list.draw(screen)

        pygame.display.flip()
        print(switch)
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
