def Exit():
    pygame.quit()
    sys.exit()
    def Press_Key_shortcut():
        while True:
            for event in pygame.event.get():
                if event .type == QUIT:
                    Exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            Exit()
                            return
def player_crash(pl_crashRect,opponent):
    for ado in opponent:
        if pl_crashRect.collodirect(ado['rect']):
            return True
    return False
def txt_objects(t,f,s,x,y):
    txt_objects = f.render(t,1,txt_c)
    txt_Rect = txt_objects.get_rect()
    txt_Rect.topleft = (x,y)
    s.blit(txt_objects,txt_Rect)


pygame.init()
time_clock = pygame.time.Clock()
screen_display_window = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('car race')
pygame.mouse.set_visible(False)

frontsize = pygame.front.SysFont(None,30)

game_over_music = pygame.mixer.Sound('audio_sound/crash.wav')
pygame.mixer.music.load('ausio_sound/car.wav')
chuckle = pygame.mixer.Sound('audio_sound/chuckle.wav')
player_car_photo = pygame.image.load('image/computer_car1.png')
computer_car3 = pygame.image.load('image/computer_car3.png')
computer_car4 = pygame.image.load('image/computer_car4.png')
gamer_Rect = player_car-photo.get_rect()
computer_car_photo = pygame.image.load('image/computer_car2.png')
another = [computer_car3,computer_car4,computer_car_photo]
w_left = pygame.image.load('image/left_side.png')
w_right = pygame.image.load('image/right_side.png')