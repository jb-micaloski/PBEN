# -*- mode: python ; coding: utf-8 -*-

import os
from kivy_deps import sdl2, glew


block_cipher = None


a = Analysis(['interface.py'],
             pathex=[],
             binaries=[],
             datas=[('ControleGeral.kv','.'),('*.py','.'),('*.png','.'),('teste.ods','.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='interface',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               Tree('C:\\Users\\lucas\\.virtualenvs\\WORLDGOD\\share\\sdl2\\bin\\'),
               Tree('C:\\Users\\lucas\\.virtualenvs\\WORLDGOD\share\\glew\\'), 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='interface')
