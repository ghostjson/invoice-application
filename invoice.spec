# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['invoice.py'],
             pathex=['/media/ghostjson/My Passport/workspace/workspace/freelance/nandorock4c/app'],
             binaries=[],
             datas=[('/usr/local/lib/python3.8/dist-packages/eel/eel.js', 'eel'), ('ui', 'ui')],
             hiddenimports=['bottle_websocket'],
             hookspath=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='invoice',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
