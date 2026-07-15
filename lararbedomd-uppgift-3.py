"""
Lärarbedömd uppgift 3 - Programmering nivå 2
Alternativ 1: Bibliotekssystem

Klasser: Book, Member (bas), StudentMedlem (arv), Library
"""


class Book:
    """En bok i biblioteket."""

    def __init__(self, titel, forfattare, isbn):
        self.titel = titel
        self.forfattare = forfattare
        self.isbn = isbn
        self.tillganglig = True  # True = inte utlånad

    def visa_info(self):
        status = "Tillgänglig" if self.tillganglig else "Utlånad"
        print(f"  '{self.titel}' av {self.forfattare} (ISBN: {self.isbn}) - {status}")


class Member:
    """Basklass för en bibliotekmedlem."""

    def __init__(self, namn, medlemsnummer):
        self.namn = namn
        self.medlemsnummer = medlemsnummer
        self.lanade_bocker = []  # lista av Book-objekt
        self.max_lan = 3  # standardgräns för antal samtidiga lån

    def lana_bok(self, bok):
        # Lånar en bok om den är tillgänglig och gränsen inte är nådd
        if not bok.tillganglig:
            print(f"{self.namn}: kan inte låna '{bok.titel}', den är redan utlånad.")
            return
        if len(self.lanade_bocker) >= self.max_lan:
            print(f"{self.namn}: har redan nått gränsen på {self.max_lan} lånade böcker.")
            return
        bok.tillganglig = False
        self.lanade_bocker.append(bok)
        print(f"{self.namn}: lånade '{bok.titel}'.")

    def lamna_tillbaka(self, bok):
        # Lämnar tillbaka en bok om medlemmen faktiskt har lånat den
        if bok in self.lanade_bocker:
            bok.tillganglig = True
            self.lanade_bocker.remove(bok)
            print(f"{self.namn}: lämnade tillbaka '{bok.titel}'.")
        else:
            print(f"{self.namn}: har inte lånat '{bok.titel}'.")

    def visa_info(self):
        print(f"Medlem: {self.namn} (nr {self.medlemsnummer}), max {self.max_lan} lån")
        if self.lanade_bocker:
            for bok in self.lanade_bocker:
                print(f"  Lånad: {bok.titel}")
        else:
            print("  Inga lånade böcker just nu.")


class StudentMedlem(Member):
    """Studentmedlem - får låna fler böcker samtidigt än en vanlig medlem."""

    def __init__(self, namn, medlemsnummer, skola):
        super().__init__(namn, medlemsnummer)
        self.skola = skola
        self.max_lan = 6  # studenter får låna dubbelt så många böcker

    def visa_info(self):
        # Utökar basklassens visa_info med skolinformation
        super().visa_info()
        print(f"  Skola: {self.skola}")


class Library:
    """Biblioteket - håller reda på alla böcker och medlemmar."""

    def __init__(self, namn):
        self.namn = namn
        self.bocker = []
        self.medlemmar = []

    def lagg_till_bok(self, bok):
        self.bocker.append(bok)
        print(f"Bok tillagd: {bok.titel}")

    def registrera_medlem(self, medlem):
        self.medlemmar.append(medlem)
        print(f"Medlem registrerad: {medlem.namn}")

    def visa_tillgangliga_bocker(self):
        print(f"\n--- Tillgängliga böcker på {self.namn} ---")
        tillgangliga = [b for b in self.bocker if b.tillganglig]
        if not tillgangliga:
            print("  Inga tillgängliga böcker just nu.")
        for bok in tillgangliga:
            bok.visa_info()

    def visa_alla_medlemmar(self):
        print(f"\n--- Medlemmar på {self.namn} ---")
        for medlem in self.medlemmar:
            medlem.visa_info()
            print()


def main():
    # Skapar biblioteket
    bibliotek = Library("Stadsbiblioteket")

    # Skapar böcker
    bok1 = Book("Python Crash Course", "Eric Matthes", "978-1")
    bok2 = Book("Clean Code", "Robert Martin", "978-2")
    bok3 = Book("Sagan om ringen", "J.R.R. Tolkien", "978-3")

    bibliotek.lagg_till_bok(bok1)
    bibliotek.lagg_till_bok(bok2)
    bibliotek.lagg_till_bok(bok3)

    # Skapar medlemmar - en vanlig och en student
    medlem1 = Member("Anna Karlsson", "M001")
    student1 = StudentMedlem("Erik Nilsson", "M002", "KTH")

    bibliotek.registrera_medlem(medlem1)
    bibliotek.registrera_medlem(student1)

    # Visar tillgängliga böcker innan lån
    bibliotek.visa_tillgangliga_bocker()

    # Lånar böcker
    medlem1.lana_bok(bok1)
    student1.lana_bok(bok2)
    student1.lana_bok(bok3)

    # Försök låna en redan utlånad bok - ska misslyckas
    medlem1.lana_bok(bok2)

    # Visar status efter lån
    bibliotek.visa_tillgangliga_bocker()
    bibliotek.visa_alla_medlemmar()

    # Lämnar tillbaka en bok
    student1.lamna_tillbaka(bok2)

    # Visar status efter återlämning
    bibliotek.visa_tillgangliga_bocker()


if __name__ == "__main__":
    main()