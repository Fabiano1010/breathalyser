from tkinter import *
import customtkinter
from customtkinter import *
import sys

# podstawowe ustawienia ------------------------------
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

# klasa -----------------------------------------------
class App(customtkinter.CTk):
    # kontruktor --------------------------------------
    def __init__(self):
        # struktura okna ------------------------------
        super().__init__()
        self.title("Alkomat")
        self.minsize(700, 800)
        # self.iconbitmap("icon.ico")

        # struktura funkcjonalna ----------------------
        label=customtkinter.CTkLabel(master=self, text="ALKOMAT", font=("Arial", 35), text_color="#02c7d1")
        label.pack(padx=20, pady=20)

        self.plec = IntVar(0)
        self.jedzenie = IntVar(0)
        self.picie = IntVar()
        self.ilosc = IntVar()
        self.waga = IntVar()

        self.slider_var = DoubleVar()


        # self.wyniki = self.czas_wydalania()


        # -------------------------------------
        self.label_result = customtkinter.CTkLabel(master=self, text="", font=("Arial", 20))
        self.label_result.pack(padx=20, pady=20, side=RIGHT)

        label=customtkinter.CTkLabel(master=self, text="Waga",font=("Arial", 15))
        label.pack(padx=20)
        self.waga_input = customtkinter.CTkEntry(master=self, placeholder_text="Waga", width=180, textvariable=self.waga  )
        self.waga_input.pack(padx=20)

        # -------------------------------------

        label=customtkinter.CTkLabel(master=self, text="Ilość wypitego trunku (ml)", font=("Arial", 15))
        label.pack(padx=20)
        self.ilosc_input = customtkinter.CTkEntry(master=self, placeholder_text="Ilość wypitego trunku (ml)", width=180, textvariable=self.ilosc)
        self.ilosc_input.pack(padx=20)

        # ------------------------------------

        label = customtkinter.CTkLabel(master=self, text="Długość picia (min)", font=("Arial", 15))
        label.pack(padx=20)

        self.dlugosc_input = customtkinter.CTkEntry(master=self, placeholder_text="Długość picia", width=180, textvariable=self.picie)
        self.dlugosc_input.pack(padx=20)

        # ------------------------------------

        label = customtkinter.CTkLabel(master=self, text="Procentowa zawartość alkoholu w trunku",font=("Arial", 15))
        label.pack(padx=20)

        self.procenty = customtkinter.CTkSlider(master=self, from_=0, to=60, command=self.slider_event, variable=self.slider_var, progress_color="#009ca3", button_color="#02c7d1", button_hover_color="#009ca3")
        self.procenty.pack(padx=20)

        self.label_procenty = customtkinter.CTkLabel(master=self, text="0%", font=("Arial", 15))
        self.label_procenty.pack(padx=20)

        # ------------------------------------

        self.plec_radio1 = customtkinter.CTkRadioButton(master=self, text="Mężczyzna", command=self.plec_fun, variable=self.plec, value=0, hover_color="#02c7d1", fg_color="#02c7d1",font=("Arial", 13))
        self.plec_radio2 = customtkinter.CTkRadioButton(master=self, text="Kobieta",command=self.plec_fun, variable=self.plec, value=1, hover_color="#02c7d1", fg_color="#02c7d1",font=("Arial", 13))

        self.plec_radio1.pack(padx=20, pady=10)
        self.plec_radio2.pack(padx=20, pady=10)

        # ------------------------------------

        label = customtkinter.CTkLabel(master=self, text="Spożycie:", font=("Arial", 15))
        label.pack(padx=20)

        self.jedzenie_radio1 = customtkinter.CTkRadioButton(master=self, text="Na czczo", command=self.wchlanianie, variable=self.jedzenie, value=0, hover_color="#02c7d1", fg_color="#02c7d1",font=("Arial", 13))
        self.jedzenie_radio2 = customtkinter.CTkRadioButton(master=self, text="Zapełniony żołądek",command=self.wchlanianie, variable=self.jedzenie, value=1, hover_color="#02c7d1", fg_color="#02c7d1",font=("Arial", 13))

        self.jedzenie_radio1.pack(padx=20, pady=10)
        self.jedzenie_radio2.pack(padx=20, pady=10)


        # ------------------------------------

        self.button = customtkinter.CTkButton(master=self, command=self.wypisz, text="Licz", fg_color="transparent",hover_color="#02c7d1", border_color="#02c7d1", border_width=1, font=("Arial", 13))
        self.button.pack(padx=20, pady=20)
        self.button = customtkinter.CTkButton(master=self, command=self.clear, text="Czyść",fg_color="transparent", hover_color="#02c7d1", border_color="#02c7d1", border_width=1,font=("Arial", 13))
        self.button.pack(padx=20)

        # -----------------------------------


        # self.ilosc_input.delete(0, END)
        # self.waga_input.delete(0, END)
        # self.dlugosc_input.delete(0, END)

    # funkcje------------------------------------------
    def slider_event(self, value):
        input = str(int(value)) + "%"
        self.label_procenty.configure(text=input)
        return int(self.slider_var.get())
    def clear(self):
        self.ilosc_input.delete(0, END)
        self.waga_input.delete(0, END)
        self.dlugosc_input.delete(0, END)
        self.label_result.configure(text="")
    # ---------------------------------------------------

    def alko(self):
        alkohol = self.ilosc.get() * int(self.slider_var.get()) * 0.79 * 0.01
        return alkohol

    def wchlanianie(self):
        if int(self.jedzenie.get()) == 0:
            return 30
        return 120


    def plec_fun(self):
        if self.plec.get() == 0:
            return 0.6
        return 0.7

    def plyny(self):
            return float(self.waga.get()) * float(self.plec_fun())


    def promile_minuta(self):
        return float(self.alko())/ float(self.plyny()) / float(self.picie.get())

    def wchlanianie_minuta(self):
        return float(self.promile_minuta()) / float(self.wchlanianie())

    def wydalanie_alko(self, alko_we_krwi):
        alko_we_krwi -= 0.12 / 60
        if alko_we_krwi < 0:
            alko_we_krwi = 0
        return alko_we_krwi

# -----------------------------

    def czas_wydalania(self):
        wydalenie_min = [0]
        alko_we_krwi = 0
        picie = 1
        picie_max = False
        wchlanianie = int(self.picie.get() + self.wchlanianie())

        for i in range(1, wchlanianie):
            alko_we_krwi += self.wchlanianie_minuta() * picie
            wydalenie_min.append(alko_we_krwi)
            if picie < self.picie.get() and not picie_max:
                picie += 1
            else:
                picie_max = True
            if i >= self.wchlanianie():
                picie -= 1
            alko_we_krwi = self.wydalanie_alko(alko_we_krwi)

        while alko_we_krwi > 0:
            alko_we_krwi = self.wydalanie_alko(alko_we_krwi)
            wydalenie_min.append(alko_we_krwi)
        return wydalenie_min


    def wypisz(self):
        wynik = ''
        czas_wydalania=self.czas_wydalania()
        for i in range(0, len(czas_wydalania), 60):
            wynik += f'{i:02}min - {czas_wydalania[i]:.2f}  ‰\n'
        self.label_result.configure(text = wynik)



#     działanie aplikacji -----------------------------

if __name__ == "__main__":
    app=App()
    app.mainloop()



