import pygame
import sys
import random

# Initialiser Pygame
pygame.init()

# Taille de la fenêtre
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quiz Capitale Mondial")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GRAY = (200, 200, 200)

# Police
font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 28)

# Liste simplifiée de pays et capitales
# Pour le vrai jeu, tu peux compléter avec tous les pays du monde
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Spain": "Madrid",
    "Italy": "Rome",
    "United Kingdom": "London",
    "USA": "Washington",
    "Canada": "Ottawa",
    "Japan": "Tokyo",
    "China": "Beijing",
    "Brazil": "Brasilia",
    "India": "New Delhi",
    "Russia": "Moscow"
}

countries = list(capitals.keys())
score = 0

# Fonctions pour générer une question
def generate_question():
    country = random.choice(countries)
    correct_answer = capitals[country]
    
    # Choisir 2 mauvaises réponses aléatoires
    wrong_answers = list(capitals.values())
    wrong_answers.remove(correct_answer)
    options = random.sample(wrong_answers, 2) + [correct_answer]
    random.shuffle(options)
    
    return country, correct_answer, options

# Boutons
button_width, button_height = 200, 50
buttons = [pygame.Rect(100 + i*250, 350, button_width, button_height) for i in range(3)]

# Générer première question
country, correct_answer, options = generate_question()
message = ""
message_color = BLACK

# Boucle du jeu
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            for i, button in enumerate(buttons):
                if button.collidepoint(mx, my):
                    if options[i] == correct_answer:
                        message = "Correct ! 🎉"
                        message_color = GREEN
                        score += 1
                    else:
                        message = f"Faux ❌ La bonne réponse était {correct_answer}"
                        message_color = RED
                    # Générer nouvelle question
                    country, correct_answer, options = generate_question()

    # Afficher score
    score_text = small_font.render(f"Score : {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Afficher question
    question_text = font.render(f"Quelle est la capitale de {country} ?", True, BLACK)
    screen.blit(question_text, (50, 150))

    # Afficher boutons
    for i, button in enumerate(buttons):
        pygame.draw.rect(screen, GRAY, button)
        opt_text = small_font.render(options[i], True, BLACK)
        text_rect = opt_text.get_rect(center=button.center)
        screen.blit(opt_text, text_rect)

    # Afficher message
    msg_text = font.render(message, True, message_color)
    screen.blit(msg_text, (WIDTH//2 - msg_text.get_width()//2, 250))

    pygame.display.update()

pygame.quit()
sys.exit()