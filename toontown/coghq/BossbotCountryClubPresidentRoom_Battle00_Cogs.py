from SpecImports import *
from toontown.toonbase import ToontownGlobals
CogParent = 110400
BattleCellId = 0
BattleCells = {BattleCellId: {'parentEntId': CogParent,
                'pos': Point3(0, 0, 0)}}
CogData = [{'type': 'cp', 'parentEntId': CogParent,
  'boss': 1,
  'level': 14,
  'battleCell': BattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'forceType': True,
  'skeleton': 0,
  'revives': 1},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': ToontownGlobals.BossbotCountryClubCogLevel,
  'battleCell': BattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'forceType': True,
  'revives': 1},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': ToontownGlobals.BossbotCountryClubCogLevel,
  'battleCell': BattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': ToontownGlobals.BossbotCountryClubCogLevel,
  'battleCell': BattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': 1}]
ReserveCogData = []
