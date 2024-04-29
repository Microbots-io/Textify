import speech_recognition as sr
import pyautogui
name = input("Wpisz swoje imię:")
def sluchaj_i_zapisuj():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Zacznij mówić...")
        recognizer.adjust_for_ambient_noise(source)
        while True:
            audio = recognizer.listen(source)

            try:
                tekst = recognizer.recognize_google(audio, language="pl-PL")
                print(name + ":" + tekst)
                with open("zapis_mowy.txt", "a") as plik:
                    plik.write(tekst + "\n")
            except sr.UnknownValueError:
                print("Nie można rozpoznać mowy")
            except sr.RequestError as e:
                print("Błąd z usługą Google: {0}".format(e))

if __name__ == "__main__":
    sluchaj_i_zapisuj()
