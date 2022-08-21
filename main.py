from azaan_app import Azaan
from datetime import datetime
from playsound import playsound

azaan = Azaan()

fazr = azaan.get_salah_time(1)
dhur = azaan.get_salah_time(2)
asar = azaan.get_salah_time(3)
magrib=azaan.get_salah_time(4)
isha = azaan.get_salah_time(5)
jummah=azaan.get_jummah_time()


prayer_times = [fazr,dhur,jummah,asar,magrib,isha]
# print(prayer_times)

while True:
    for azaan_time in prayer_times:
        currenttime = datetime.now().strftime("%H:%M:%p")
        if str(currenttime) == azaan_time:
            print(azaan_time)
            playsound("azaan.mp3")
