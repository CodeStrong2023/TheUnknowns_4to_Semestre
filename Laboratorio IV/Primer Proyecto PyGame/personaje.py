import pygame

pygame.init()

# Configuracion de pantalla
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
dt = 0

# Posicion del jugador
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Velocidad del jugador
player_speed = 5

# Bucle principal para mover al jugador
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Como se va a mover el jugador
    # Detectar las teclas para presionar
    keys = pygame.key.get_pressed()

    # Movimiento del jugador (teclas de flechas)
    if keys[pygame.K_LEFT]:    # Se presiona la tecla izquierda
        player_pos.x -= player_speed
    if keys[pygame.K_RIGHT]:    #Se presiona la tecla hacia la derecha
        player_pos.x += player_speed
    if keys[pygame.K_DOWN]:  # Se presiona la tecla hacia abajo
        player_pos.y += player_speed
    if keys[pygame.K_UP]:       # Se presiona la tecla hacia arriba
        player_pos.y -= player_speed

    # Limpiar la pantalla
    screen.fill("green")

    # Dibujar el jugador (en este caso es un circulo rojo)
    pygame.draw.circle(screen, (255, 0, 0), center=(int(player_pos.x), int(player_pos.y)), radius=10)

    # Actualizar pantalla
    pygame.display.flip()

    # Control de velocidad del jugador, frames por segundo (dt)
    clock.tick(60)


pygame.quit() # Cierre del programa