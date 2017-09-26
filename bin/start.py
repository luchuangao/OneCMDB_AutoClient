import os
os.environ['USER_SETTINGS'] = "config.settings"

from lib.conf.config import settings

print(settings.USER)
print(settings.EMAIL)



