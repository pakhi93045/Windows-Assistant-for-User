import datetime
import winsound
import speech_recognition as sr

def alarm(Timing):
    alttime = str(datetime.datetime.strptime(Timing, "%I:%M %p"))
    alttime = alttime[11:-3]
    print(f"Parsed alarm time: {alttime}")

    # Extract hours and minutes from the parsed time
    Horeal = alttime[:2]
    Horeal = int(Horeal)
    Mireal = alttime[3:5]
    Mireal = int(Mireal)
    print(f"Done, alarm is set for {Timing}")

        # Alarm loop
    while True:
        if Horeal == datetime.datetime.now().hour:
            if Mireal == datetime.datetime.now().minute:
                print("Alarm is running")
                winsound.PlaySound('abc', winsound.SND_LOOP)

                  
            elif Mireal < datetime.datetime.now().minute:
                break

   



if __name__ == '__main__':
    # Assuming 'tt' is the time you are passing to the alarm function
    tt = input("Enter the time for alarm (e.g., '12:44 AM'): ").strip()
    alarm(tt)
