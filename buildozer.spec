[app]
title = MyVPN
package.name = myvpn
package.domain = com.myvpn

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf

version = 0.1

# کتابخانه‌های مورد نیاز
requirements = python3==3.11.5,kivy==2.3.0,kivymd==1.1.1,pyjnius==1.6.1,requests,urllib3

orientation = portrait
fullscreen = 0

# آیکون
icon.filename = %(source.dir)s/icon.png

# ⚠️ مجوزهای مهم برای VPN
android.permissions = \
    android.permission.INTERNET,\
    android.permission.ACCESS_NETWORK_STATE,\
    android.permission.ACCESS_WIFI_STATE,\
    android.permission.FOREGROUND_SERVICE,\
    android.permission.BIND_VPN_SERVICE,\
    android.permission.POST_NOTIFICATIONS

android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a
android.allow_backup = False

# امنیت
android.debug_artifact = apk
android.release_artifact = aab

[buildozer]
log_level = 2
warn_on_root = 1
