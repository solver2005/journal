[app]
title = SchApp
package.name = schapp
package.domain = org.example
source.dir = .
source.include_exts = py,kv
version = 0.1
requirements = python3,kivy[full]==2.1.0,cython

android.api = 33
android.minapi = 21
android.ndk_api = 21
orientation = landscape
android.permissions = INTERNET, ACCESS_NETWORK_STATE #Удалите, если не используете интернет