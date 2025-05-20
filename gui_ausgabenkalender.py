import tkinter as tk

transactions = []

def transaktion_speichern():
    typ = typ_eingabe.get()
    betrag = float(betrag_eingabe.get())
    kategorie = kategorie_eingabe.get()
    beschreibung = beschreibung_eingabe.get()

    eintrag = {
        "typ": typ,
        "betrag": betrag,
        "kategorie": kategorie,
        "beschreibung": beschreibung
    }
    transactions.append(eintrag)

    ausgabe_label.config(text="♡ Transaktion gespeichert!", fg="#b388eb")

    # Anzeige aktualisieren
    anzeige.config(state="normal")
    anzeige.delete("1.0", tk.END)
    for t in transactions:
        zeile = f"{t['typ']} - {t['betrag']}€ - {t['kategorie']} ({t['beschreibung']})\n"
        anzeige.insert(tk.END, zeile)
    anzeige.config(state="disabled")

# Fenster
fenster = tk.Tk()
fenster.title("Haushaltsbuch GUI")
fenster.geometry("430x500")
fenster.configure(bg="#f8f4ff")  # Pastell-Hintergrund

# Styling-Font
label_font = ("Segoe UI", 11)
entry_font = ("Segoe UI", 10)

# Funktion zum Label/Entry-Paketieren
def feld(label_text):
    lbl = tk.Label(fenster, text=label_text, font=label_font, bg="#f8f4ff")
    lbl.pack(pady=(8, 0))
    entry = tk.Entry(fenster, font=entry_font)
    entry.pack(pady=(0, 4))
    return entry

# Felder
typ_eingabe = feld("Typ (Einnahme/Ausgabe):")
betrag_eingabe = feld("Betrag (€):")
kategorie_eingabe = feld("Kategorie:")
beschreibung_eingabe = feld("Notiz:")

# Button
tk.Button(fenster, text="Transaktion speichern", font=label_font, bg="#d1c4e9", command=transaktion_speichern).pack(pady=12)

# Textfeld
anzeige = tk.Text(fenster, height=10, width=45, font=("Courier New", 10), state="disabled", bg="#ffffff")
anzeige.pack(pady=10)

# Feedback-Label
ausgabe_label = tk.Label(fenster, text="", font=("Segoe UI", 10, "italic"), bg="#f8f4ff")
ausgabe_label.pack()

# GUI starten
fenster.mainloop()
