from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

class Player(FirstPersonController):
    def __init__(self):  # __int__ -> __init__
        super().__init__(
            speed=10,
            model='cube',
            collider='box',
            scale=1
        )

class Exit(Entity):
    def __init__(self, x, z):
        super().__init__(
            model='cube',
            color=color.black90,
            position=(x*5, 0, z*5),
            scale=(5, 5, 5)
        )
        
        self.clear = Text(
            text='clear',
            scale=2,
            origin=(0, 0),
            visible=False
        )

    def update(self):
        # Player 인스턴스를 여기에서 직접 참조해야 함
        if player.intersects(self).hit:
            self.clear.visible = True
            player.enabled = False

class Enemy(Entity):
    def __init__(self, x, y):
        super().__init__(
            model='cube',
            color=color.black,
            scale=0.5,
            position=(x*5, 1, y*5),
            collider='box',
            rotation=(0, 90, 0)
        )
        self.start = self.position  # start를 self.position으로 수정

    def update(self):
        self.position += Vec3(0.05, 0, 0)

        if self.intersects(player).hit:  # player 인스턴스
            player.position = (50, 0, 55)

        for wall in walls:
            if self.intersects(wall).hit:
                self.position = self.start

class Wrap(Entity):
    def __init__(self, x, y):
        super().__init__(
            model='cube',
            color=color.black,
            scale=5,
            position=(x*5, 0, y*5),
            collider='box'
        )

    def update(self):
        if self.intersects(player).hit:  # player 인스턴스
            player.position = (50, 0, 55)

# Ground
ground = Entity(
    model='plane',
    color=color.gray,
    position=(0, -1, 0),
    scale=(200, 1, 200),
    collider='mesh'
)

# Map 설정
Map = [
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 'e', 29, 30],
    [11, 12, 13, 14, 15, 16, 17, None, 19, 20, 21, 22, None, None, None, None, 27, None, 29, 30],
    # ... (여기에 나머지 맵을 추가)
]

walls = []
player = Player()  # Player 인스턴스 생성

for i in range(len(Map)):
    for j in range(len(Map[i])):
        if Map[i][j]:
            if Map[i][j] == 'p':
                player.position = (i * 5, 0, j * 5)
                continue
            if Map[i][j] == 'e':
                exit = Exit(i, j)
                continue
            if Map[i][j] == 'x':
                enemy = Enemy(i, j)
                continue
            if Map[i][j] == 'w':
                wrap = Wrap(i, j)
                continue
            cube = Entity(
                model='cube',
                color=color.white,
                position=(i * 5, 0, j * 5),
                collider='box',
                scale=5
            )
            walls.append(cube)

app.run()
