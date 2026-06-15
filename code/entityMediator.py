from code.Const import WIN_WIDTH
from code.entity import Entity
from code.enemy import Enemy
from code.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0

        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0

        if isinstance(ent, PlayerShot):
            if ent.rect.left <= 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for ent in entity_list:
            EntityMediator.verify_collision_window(ent)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list[:]:  # cópia da lista (evita bug ao remover)
            if ent.health <= 0:
                entity_list.remove(ent)
