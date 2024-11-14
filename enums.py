from enum import Enum


class CharacterSkins(Enum):

    MEN1 = 'men1'
    MEN2 = 'men2'
    MEN3 = 'men3'
    WOMEN1 = 'women1'
    WOMEN2 = 'women2'
    WOMEN3 = 'women3'

    MALE_SKINS = [
        MEN1,
        MEN2,
        MEN3,
    ]

    FEMALE_SKINS = [
        WOMEN1,
        WOMEN2,
        WOMEN3,
    ]

class CharacterSex(Enum):

    MALE = 'm'
    FEMALE = 'f'
    RANDOM = 'r'

    SEX_SKIN_MAP = {
        'm': CharacterSkins.MALE_SKINS.value,
        'f': CharacterSkins.FEMALE_SKINS.value,
        'r': CharacterSkins.MALE_SKINS.value + CharacterSkins.FEMALE_SKINS.value,
    }

class TileTypes(Enum):

    MONSTER = 'monster'
    RESOURCE = 'resource'
    WORKSHOP = 'workshop'
    BANK = 'bank'
    GRAND_EXCHANGE = 'grand_exchange'
    TASKS_MASTER = 'tasks_master'


class ActionType(Enum):

    MOVE = 'move'
    EQUIP = 'equip'
    UNEQUIP = 'unequip'
    FIGHT = 'fight'
    GATHERING = 'gathering'
    CRAFTING = 'crafting'
    RECYCLING = 'recycling'
    USE = "use"
    DELETE = 'delete'
    NEW_TASK = 'new task'
    COMPLETE_TASK = 'complete task'
    EXCHANGE_TASK = 'exchange task coins'
    TRADE_TASK = 'trade task'
    CANCEL_TASK = 'cancel task'
    BUY_ITEM = 'buy item'
    SELL_ITEM = 'sell item'
    CANCEL_SALE = 'cancel sale'
    DEPOSIT_BANK = 'deposit item'
    DEPOSIT_BANK_GOLD = 'deposit gold'
    WITHDRAW_BANK = 'withdraw item'
    WITHDRAW_GOLD = 'withdraw gold'
    BUY_EXPANSION = 'buy expanion',
    REST = 'rest'

    RUN_PREMADE_ACTIONS = 'run premade actions'

    AVAILABLE_ACTIONS = [
        MOVE,
        FIGHT,
        GATHERING,
        CRAFTING,
        EQUIP,
        UNEQUIP,
        NEW_TASK,
        COMPLETE_TASK,
        BUY_ITEM,
        SELL_ITEM,
        DELETE,
        REST,
        RUN_PREMADE_ACTIONS,
    ]

    LOCATION_ACTIONS_MAP = {
        None: [
            MOVE,
            EQUIP,
            UNEQUIP,
            USE,
            REST,
            RUN_PREMADE_ACTIONS,
        ],
        TileTypes.MONSTER.value: [
            MOVE,
            FIGHT,
            EQUIP,
            UNEQUIP,
            USE,
            RUN_PREMADE_ACTIONS,
        ],
        TileTypes.RESOURCE.value: [
            MOVE,
            GATHERING,
            EQUIP,
            UNEQUIP,
            USE,
            RUN_PREMADE_ACTIONS,
        ],
        TileTypes.WORKSHOP.value: [
            MOVE,
            CRAFTING,
            RECYCLING,
            EQUIP,
            UNEQUIP,
            USE,
            RUN_PREMADE_ACTIONS,
        ],
        TileTypes.BANK.value: [
            MOVE,
            EQUIP,
            UNEQUIP,
            DEPOSIT_BANK,
            DEPOSIT_BANK_GOLD,
            WITHDRAW_BANK,
            WITHDRAW_GOLD,
            USE,
            BUY_EXPANSION,
            RUN_PREMADE_ACTIONS,
        ],
        TileTypes.GRAND_EXCHANGE.value: [
            MOVE,
            EQUIP,
            UNEQUIP,
            BUY_ITEM,
            SELL_ITEM,
            USE,
            CANCEL_SALE,
            RUN_PREMADE_ACTIONS,
        ],
        TileTypes.TASKS_MASTER.value: [
            MOVE,
            EQUIP,
            UNEQUIP,
            NEW_TASK,
            COMPLETE_TASK,
            EXCHANGE_TASK,
            TRADE_TASK,
            CANCEL_SALE,
            RUN_PREMADE_ACTIONS,
        ],
    }

class CraftSkill(Enum):

    WEAPONCRAFTING = 'weaponcrafting'
    GEARCRAFTING = 'gearcrafting'
    JEWELRYCRAFTING = 'jewelrycrafting'
    COOKING = 'cooking'
    WOODCUTTING = 'woodcutting'
    MINING = 'mining'
    FISHING = 'fishing'
    ALCHEMY = 'alchemy'

class ItemTypes(Enum):

    CONSUMABLE = 'consumable'
    BODY_ARMOR = 'body_armor'
    WEAPON = 'weapon'
    RESOURCE = 'resource'
    LEG_ARMOR = 'leg_armor'
    HELMET = 'helmet'
    BOOTS = 'boots'
    SHIELD = 'shield'
    AMULET = 'amulet'
    RING = 'ring',
    CURRENCY = 'currency',
    UTILITY = 'utility',
    ARTIFACT = 'artifact'

    EQUIP_TYPES = [
        CONSUMABLE,
        BODY_ARMOR,
        WEAPON,
        LEG_ARMOR,
        HELMET,
        BOOTS,
        SHIELD,
        AMULET,
        RING,
        ARTIFACT,
    ]

class EquipmentSlots(Enum):

    WEAPON = 'weapon'
    SHIELD = 'shield'
    HELMET = 'helmet'
    BODY_ARMOR = 'body_armor'
    LEG_ARMOR = 'leg_armor'
    BOOTS = 'boots'
    RING1 = 'ring1'
    RING2 = 'ring2'
    AMULET = 'amulet'
    ARTIFACT1 = 'artifact1'
    ARTIFACT2 = 'artifact2'
    ARTIFACT3 = 'artifact3'
    CONSUMABLE1 = 'consumable1'
    CONSUMABLE2 = 'consumable2'

class TaskTypeEnum(Enum):

    MONSTERS = 'monsters'
    ITEMS = 'items'