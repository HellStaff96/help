from pygame import *
init()
level1 = [
    "r                                                                    .",
    "r                                                                    .",
    "r                                                                    .",
    "r                                                                    .",
    "rr    °  °      l                             r    °  °  °     l     .",
    "r  ------------                                ---------------       .",
    "rr / l                                       r / l         r / l     .",
    "rr   l                                       r   l         r   l     .",
    "rr     °  l                       r     °  °     l   r         l     .",
    "r  ------                           ------------       -------       .",
    "r     r / l                                          r / l           .",
    "r     r   l                                          r   l           .",
    "r     r       °  °   l                       r   °  °    l           .",
    "r       ------------                           ---------             .",
    "r                r / l                       r / l                   .",
    "r                r   l                       r   l                   .",
    "r                                 k                                  .",
    "----------------------------------------------------------------------"] #Матір Божьє это уровень 

level1_width = len(level1[0]) * 48  # Ширина уровня
lever_height = len(level1) * 40     # Высота уровня

W = 1280
H = 720


window = display.set_mode((W, H))
back = transform.scale(image.load('Custom/Moony.png'), (W, H))
display.set_caption('Ори но с арабского сайта 🤑')
display.set_icon(image.load('images/portal.png')) # Иконка окна

''''Тута картиночки :3'''

# Спрайт игрока
hero_r = "Custom/Nedo_Ori_r.png"
hero_l = "Custom/Nedo_Ori_l.png"
# Спрайт врага
enemy_r = "Custom/Nechest_l.png"
enemy_l = "Custom/Nechest_r.png"
# Спрайт монеточЕк 
coin_img = "Custom/Monetka.png"

door_img = "images/door.png" # Спрайт дверей
key_img = "images/key.png"# Спрайт ключа
# Спрайты Сундука
chest_open = "images/cst_open.png"
chest_close = "images/cst_close.png"

stairs = "images/stair.png"# Спрайт лестницы
portal_img = "images/portal.png" # Спрайт порталаа
platform = "Custom/Grass.png" # Спрайт платформы
power = "images/mana.png" # Мана какая-то О_о
nothing = "images/nothing.png" # Спрайт... ааээ.. Пустоты?

font2 = font.SysFont(('font/ariblk.ttf'), 60)
e_tap = font2.render('press (e)', True, (255, 0, 255))
k_need = font2.render('You need a key to open!', True, (255, 0, 255))
space = font2.render('press (space) to kill the enemy', True, (255, 0, 255))
#font1 = font.SysFont(('font/impact.ttf'), 60)

class Settings(sprite.Sprite): # Это - база 😋
    def __init__(self, x, y, width, height, speed, img):
        super().__init__()
        self.width = width
        self.height = height
        self.speed = speed
        self.image = transform.scale(image.load(img), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):                                                                                                            #Coems🤑🤑🤑 
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Settings): #Для игрока

    def r_l(self):
        key_pressed = key.get_pressed() #
        if key_pressed[K_a]:
            self.rect.x -= self.speed
            self.image = transform.scale(image.load(hero_l), (self.width, self.height))
        if key_pressed[K_d]:
            self.rect.x += self.speed
            self.image = transform.scale(image.load(hero_r), (self.width, self.height))
    def u_d(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w]:
            self.rect.y -= self.speed
        if key_pressed[K_s]:
            self.rect.y += self.speed
            

class Enemy(Settings): #Для врага
    def __init__(self, x, y, width, height, speed, img, side):
        Settings.__init__(self, x, y, width, height, speed, img)
        self.side = side

    def update(self):
        global side 
        if self.side == 'left':
            self.rect.x -= self.speed
        if self.side == 'right':
            self.rect.x += self.speed




class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)
    
    def apply(self, target):
        return target.rect.move(self.state.topleft)
    
    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def camera_config(camera, target_rect): 
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + W / 2, -t + H / 2
    
    l = min(0, l)  # Не виходимо за ліву межу
    l = max(-(camera.width - W), l)  # Не виходимо за праву межу
    t = max(-(camera.height - H), t)  # Не виходимо за нижню межу
    t = min(0, t)  # Не виходимо за верхню межу
    
    return Rect(l, t, w, h)



def collides():
    global open_d, open_ch
    key_pressed = key.get_pressed()
    for s in stairs_lst:
        if sprite.collide_rect(hero, s):
            hero.u_d()
            if hero.rect.y < s.rect.y - 40:
                hero.rect.y = s.rect.y - 40 
            if hero.rect.y > s.rect.y + 130:
                hero.rect.y = s.rect.y + 130
    
    for l in block_l: 
        if sprite.collide_rect(hero, l):
            hero.rect.x = hero.rect.x - hero.width
        if sprite.collide_rect(Nechest1, l):
            Nechest1.side = "left"
            Nechest1.image = transform.scale(image.load(enemy_r), (Nechest1.width, Nechest1.height))
        if sprite.collide_rect(Nechest2, l):
            Nechest2.side = "left"
            Nechest2.image = transform.scale(image.load(enemy_r), (Nechest2.width, Nechest2.height))
        if sprite.collide_rect(Nechest3, l):
            Nechest3.side = "left"
            Nechest3.image = transform.scale(image.load(enemy_r), (Nechest3.width, Nechest3.height))
        if sprite.collide_rect(Nechest4, l):
            Nechest4.side = "left"
            Nechest4.image = transform.scale(image.load(enemy_r), (Nechest4.width, Nechest4.height))

    mixer.init()
    chest_opened = mixer.Sound('sounds/chest.wav')

    for r in block_r: 
        if sprite.collide_rect(hero, r):
            hero.rect.x = hero.rect.x + hero.width
        if sprite.collide_rect(Nechest1, r):
            Nechest1.side = "right"
            Nechest1.image = transform.scale(image.load(enemy_l), (Nechest1.width, Nechest1.height))
        if sprite.collide_rect(Nechest2, r):
            Nechest2.side = "right"
            Nechest2.image = transform.scale(image.load(enemy_l), (Nechest2.width, Nechest2.height))
        if sprite.collide_rect(Nechest3, r):
            Nechest3.side = "right"
            Nechest3.image = transform.scale(image.load(enemy_l), (Nechest3.width, Nechest3.height))
        if sprite.collide_rect(Nechest4, r):
            Nechest4.side = "right"
            Nechest4.image = transform.scale(image.load(enemy_l), (Nechest4.width, Nechest4.height))

    if sprite.collide_rect(hero, key1):
        window.blit(e_tap, (500, 50))
        if key_pressed[K_e]:
            items.remove(key1)
            key1.rect.y = -100
            open_ch = True

    if sprite.collide_rect(hero, chest) and open_ch == True:
        window.blit(e_tap, (500, 50))
        if key_pressed[K_e]:
            chest.image = transform.scale(image.load('images/cst_open.png'), (chest.width, chest.height))
            chest_opened.play()
            open_d = True

    if sprite.collide_rect(hero, chest) and open_ch == False:
        window.blit(k_need, (450, 50))

    

        
    if sprite.collide_rect(hero, door) and open_d == False:
        hero.rect.x = door.rect.x - hero.width
        window.blit(k_need, (450, 50))

    if sprite.collide_rect(hero, door) and open_d == True:
        window.blit(e_tap, (500, 50))
        if key_pressed[K_e]:
           door.rect.x = -2000



    coins_count = 0
    mixer.init()
    coin_collected = mixer.Sound('sounds/c_coll.wav')

    for coin in coins:
        if sprite.collide_rect(hero, coin):
            coins_count += 1
            coin_collected.play()
            items.remove(coin)
            coin.rect.y = -10000
        
    



def menu():
    pass

def rules():
    pass

def pause():
    pass

def restart():
    pass



def start_pos():
    global items
    global camera
    global hero
    global stairs_lst, block_r, block_l, plat, coins, Nechest1, Nechest2, Nechest3, Nechest4 ,key1, chest, door, open_d, open_ch
    hero = Player(300, 650, 50, 50, 5, hero_l)
    
    camera = Camera(camera_config, level1_width, lever_height) 

    key1 = Settings(450, 500, 40, 20, 0, key_img)
    chest = Settings(300, 150, 50, 50, 0, chest_close)
    door = Settings(1200, 590, 50, 100, 0, door_img)
    Nechest1 = Enemy(150, 320, 50, 50, 3, enemy_l, 'left')
    Nechest2 = Enemy(330, 470, 50, 50, 3, enemy_l, 'left')
    Nechest3 = Enemy(1700, 160, 50, 50, 3, enemy_l, 'left')
    Nechest4 = Enemy(1800, 320, 50, 50, 3, enemy_l, 'left')

    open_d = False
    open_ch = False 

    items = sprite.Group()
    
    block_r = []
    block_l = []
    plat = []
    coins = []
    stairs_lst = []
    x = 0
    y = 0

    for r in level1:
        for c in r:
            if c == '-':
                p1 = Settings(x, y, 40, 40, 0, platform)
                plat.append(p1)
                items.add(p1)
            if c == 'l':
                p2 = Settings(x, y, 40, 40, 0, nothing)
                block_l.append(p2)
                items.add(p2)
            if c == 'r':
                p3 = Settings(x, y, 40, 40, 0, nothing)
                block_r.append(p3)
                items.add(p3)
            if c == '°':
                p4 = Settings(x, y, 40, 40, 0, coin_img)
                coins.append(p4) 
                items.add(p4)
            if c == '/':
                p5 = Settings(x, y-40, 40, 180, 0, stairs) 
                stairs_lst.append(p5)
                items.add(p5)
            
            
            x += 40
        y += 40
        x = 0
    items.add(hero)
    items.add(key1)
    items.add(chest)
    items.add(door)
    items.add(Nechest1)
    items.add(Nechest2)
    items.add(Nechest3)
    items.add(Nechest4)
    

def lvl1():
    game = True
    while game:
        time.delay(5)
        window.blit(back, (0,0))
        for e in event.get():
            if e.type == QUIT:
                game = False
        camera.update(hero)
        hero.r_l()
        Nechest1.update()
        Nechest2.update()
        Nechest3.update()
        Nechest4.update()
        
        collides()
        for i in items:
            window.blit(i.image, camera.apply(i))

        display.update()

def lvl1_end():
    pass

start_pos()
lvl1()