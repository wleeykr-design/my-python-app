[app]
title = My Python App
package.name = mypyapp
package.domain = org.offline
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
