from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

class Player(FirstPersonController):
    def __init__(self):
        super().__init__(
            speed=10,
            model='cube',
            collider='box',
            scale=1
        )

# 플레이어 인스턴스 생성
player = Player()

# 바닥1 생성
ground1 = Entity(
    model='plane',
    color=color.gray,
    position=(0, 0, 0),
    scale=(200, 1, 200),
    collider='mesh'
)

# 바닥2 생성
ground2 = Entity(
    model='plane',
    color=color.gray,
    position=(0, 0, 5),  # 지면 1에서 약간 위에 위치
    scale=(3, 1, 3),
    collider='mesh'
)

# 플랫폼 생성

# 계단형 플랫폼
for i in range(4):
    Entity(
        model='cube',
        color=color.green,
        position=(2 + (i * 5), 1 + i, 0),
        scale=(3, 1, 3),
        collider='box'
    )

# 두 번째 층 플랫폼
for i in range(2):
    Entity(
        model='cube',
        color=color.green,
        position=(17, 5 + i, 5 + i * 5),
        scale=(3, 1, 3),
        collider='box'
    )

# 세 번째 층 플랫폼
for i in range(4):
    Entity(
        model='cube',
        color=color.green,
        position=(17 + (i * 5), 7 + (i * 0.5), 13),
        scale=(3, 0.1, 3),
        collider='box'
    )

# 추가 플랫폼
additional_platforms = [
    ((37, 9, 13), color.green, (3, 0.1, 9)),
    ((43, 9, 13), color.red, (6, 0.1, 3)),
    ((43, 9, 16), color.yellow, (6, 0.1, 3)),
    ((43, 9, 10), color.blue, (6, 0.1, 3)),
    ((49, 9, 16), color.green, (3, 0.1, 3)),
    ((49, 9, 20), color.yellow, (2, 2, 2), 'sphere')
]

# 추가 플랫폼 생성
for pos, color, scale, *model in additional_platforms:
    Entity(
        model=model[0] if model else 'cube',
        color=color,
        position=pos,
        scale=scale,
        collider='box'
    )



# 업데이트 함수
def update():
    # 플레이어가 ground1에 닿으면 ground2로 이동
    if player.intersects(ground1).hit:
        player.position = ground2.position + Vec3(0, 0, -5)  # ground2 위로 이동

app.run()

