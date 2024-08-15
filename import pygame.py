import pygame
# Inicializa o Pygame
pygame.init()

# Define as cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Define as dimensões da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))

# Define o título da janela
pygame.display.set_caption("Jogo Simples")

# Define a velocidade do jogador
velocidade = 5

# Define as coordenadas do jogador
x = largura // 2
y = altura // 2

# Cria o loop principal do jogo
rodando = True
while rodando:
    # Verifica os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Verifica as teclas pressionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade

    # Limpa a tela
    tela.fill(preto)

    # Desenha o jogador
    pygame.draw.rect(tela, vermelho, (x, y, 40, 40))

    # Atualiza a tela
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()