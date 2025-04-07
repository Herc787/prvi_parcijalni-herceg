# Parcijalni Ispit - Osnove Programiranja u Pythonu

## Upute za Rješavanje Zadatka

1. **Priprema okruženja:**
   - Kreirajte "fork" repozitorija.
   - Dodijelite repozitoriju naziv u formatu `prvi_parcijalni_ime_prezime` (primjer: `prvi_parcijalni_pero_peric`). 
   - **VAŽNO:** Nemojte kreirati "clone" repozitorija jer nemate pravo mijenjanja.

2. **Postavljanje Projekta:**
   - Nakon što ste kreirali fork, klonirajte repozitorij s vašeg GitHub profila na lokalno računalo koristeći GitHub Desktop ili drugu omiljenu metodu.
   - **Nakon kloniranja**, kreirajte novu lokalnu granu nazvanu `ispit`
   - Sve promjene unosite isključivo unutar grane ispit

3. **Implementacija Funkcionalnosti:**
   - Repozitorij sadrži djelomično implementiranu aplikaciju kojoj nedostaju određene funkcionalnosti.
   - Mjesta gdje treba dodati funkcionalnosti označena su komentarima `#TODO` i ključnom riječi `pass`.
   - Vaš zadatak je dopuniti funkcije, ukloniti `pass`, te ostaviti `#TODO` komentar netaknutim.

4. **Zadaci za Implementaciju:**
   - Učitavanje podataka o ponudama iz datoteke `offers.json`.
   - Kreiranje novih ponuda – unos i izbor podataka od strane korisnika.
   - Upravljanje proizvodima – kreiranje novih proizvoda te izmjena postojećih pohranjenih u `products.json`.
   - Pohrana novih ponuda u `offers.json` bez brisanja prethodnog sadržaja.
   - Ispis svih ponuda, ponuda unutar određenog mjeseca ili pojedinačne ponude.

   **VAŽNO:** Pažljivo pratite upute nakon `#TODO` komentara. U nastavku su primjeri koji ilustriraju kako bi kod trebao izgledati.

---

## Primjer Rješavanja Zadatka

### Početni Kod Funkcije

```python
# TODO: Implementirati funkciju za izračunavanje prosjeka dvaju brojeva
def calculate_average(a: float, b: float) -> float:
    pass
```

### Implementirani Kod Funkcije

```python
def calculate_average(a: float, b: float) -> float:
    if b == 0:
        print("Greška: Dijeljenje s nulom nije dozvoljeno.")
        return 0.00
    return a / b
```

> **Napomena:** Funkcija vraća `0.00` u slučaju dijeljenja s nulom, a dodatno ispisuje poruku o grešci u konzoli. Cijeli kod aplikacije mora ostati netaknut osim dodataka koje unosite na mjestima označenim komentarima `#TODO`.

### Dodatne Upute

- Nemojte mijenjati druge dijelove aplikacije. Ako Vaša implementacija ne radi, prilagodite svoje rješenje aplikaciji, a ne obrnuto.
- Uporabite `TypeHints` prema uputama u komentarima kako biste osigurali konzistentnost tipova podataka.

## Podnošenje Rješenja

1. Nakon što završite implementaciju:
   - Napravite commit za sve promjene koje ste unijeli koristeći opciju `git commit`.
   - Pushajte granu na vaš GitHub repozitorij `git push`.
  
     
2. Otvorite **Pull Request** iz grane `ispit` prema grani `main`.

   - U Pull Requestu:
     - **Autor:** Vaše ime – osoba koja je radila ispit
     - **Reviewer:** Predavač (kojem ste dali pristup kao suradniku)

       
2. **Podjela Repozitorija s Predavačem**:
   - Otvorite vaš repozitorij na GitHubu.
   - Kliknite na karticu **Settings** (Postavke) u repozitoriju.
   - Pronađite opciju **Collaborators** (Suradnici) i dodajte predavača kao **Contributor**.
   - Unesite GitHub korisničko ime predavača, odaberite ga s popisa, te mu pošaljite pozivnicu za pristup.
   - Predavač će imati pravo pregledati vaš kod i provjeriti zadatke.

> ⚠️ Provjerite da su sve promjene **commitane i pushane** prije nego što dodate predavača, kako bi mogao vidjeti kompletno rješenje.

> **Napomena:** Ako se upute ne budu striktno slijedile, ispit neće biti pregledan.

> **Rok predaje:** 7.4.2025 do 21:00h

---

**Sretno!**
