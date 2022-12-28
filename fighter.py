import pygame

class Fighter():
    def __init__(self, x, y):
        self.flip = False
        self.rect = pygame.Rect(x, y, 80, 100)
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

    def move(self, screen_width, screen_height, surface, target):
        SPEED = 5
        GRAVITY = 2
        change_x = 0
        change_y = 0

        key = pygame.key.get_pressed()

        # can do actions only when not attacking
        if self.attacking == False:

            # movement
            if key[pygame.K_a]:
                change_x = -SPEED
            if key[pygame.K_d]:
                change_x = SPEED
            
            # Jump
            if key[pygame.K_w] and self.jump == False:
                self.vel_y = -30
                self.jump = True
            
            # Attack
            if key[pygame.K_q] or key[pygame.K_e]:
                self.attack(surface, target)
                if key[pygame.K_q]:
                    self.attack_type = 1
                if key[pygame.K_e]:
                    self.attack_type = 2
        
        # Gravity things
        self.vel_y += GRAVITY
        change_y += self.vel_y
        
        # Avoid wall clipping
        if self.rect.left + change_x < 0:
            change_x = 0 - self.rect.left

        if self.rect.right + change_x > screen_width:
            change_x = screen_width - self.rect.right

        # Avoid falling off ground
        if self.rect.bottom + change_y > screen_height - 35:
            self.vel_y = 0
            self.jump = False
            change_y = screen_height - 35 - self.rect.bottom

        # fighter face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        # update position
        self.rect.x += change_x
        self.rect.y += change_y

    def attack(self, surface, target):
        self.attacking = True
        attack_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
        
        # Attack collision check
        if attack_rect.colliderect(target.rect):
            target.health -= 10

        
        pygame.draw.rect(surface, (0, 255, 0), attack_rect)