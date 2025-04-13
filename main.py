import json


OFFERS_FILE = "offers.json"
PRODUCTS_FILE = "products.json"
CUSTOMERS_FILE = "customers.json"


def load_data(filename):
    """Load data from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error decoding {filename}. Check file format.")
        return []


def save_data(filename, data):
    """Save data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# TODO: Implementirajte funkciju za kreiranje nove ponude.
def create_new_offer(offers, products, customers):
    """
    Prompt user to create a new offer by selecting a customer, entering date,
    choosing products, and calculating totals.
    """
    # Omogućite unos kupca
    # Izračunajte sub_total, tax i total
    # Dodajte novu ponudu u listu offers


    #Odabir kupaca
    print("-" * 60)
    print("Odaberite kupca:")
    for index, customer in enumerate(customers, start=1):
        print(f"{index}. {customer['name']}")
    print("-" * 60)
    
    while True:
        try:
            choice = int(input("Unesite broj kupca: "))
            if 1 <= choice <= len(customers):
                selected_customer = customers[choice - 1]
                print(f"Odabrani kupac: {selected_customer['name']}")
                break
            else:
                print("Neispravan broj, pokusajte ponovo.")
        except ValueError:
            print("Neispravan unos, morate unjeti broj!")
    
    #Datum
    offer_date = input("Unesite datum ponude (YYYY-MM-DD): ")
    
    #Odabir proizvoda
    selected_products = []
    sub_total = 0.0
    
    while True:
        print("-" * 60)
        print("Odaberite proizvod (0 za kraj):")
        for index, product in enumerate(products, start=1):
            print(f"{index}. {product['name']} - ${product['price']}")
        print("-" * 60)
        
        try:
            product_choice = int(input("Unesite broj proizvoda (0 za kraj): "))
            if product_choice == 0:
                break
            elif 1 <= product_choice <= len(products):
                selected_product = products[product_choice - 1]
                print(f"Odabrani proizvod: {selected_product['name']}")
                try:
                    quantity = int(input("Unesite količinu: "))
                    if quantity <= 0:
                        print("Količina mora biti veća od 0. Pokušajte ponovo.")
                        continue
                except ValueError:
                    print("Neispravan unos, količina mora biti broj!")
                    continue
                
                item_total = selected_product['price'] * quantity
                selected_product_item = {
                    "product_id": selected_product['id'],
                    "product_name": selected_product['name'],
                    "description": selected_product['description'],
                    "price": selected_product['price'],
                    "quantity": quantity,
                    "item_total": item_total
                }
                selected_products.append(selected_product_item)
                sub_total += item_total
                print(f"Dodano: {quantity}x {selected_product['name']} - Ukupno: ${item_total:.2f}")
            else:
                print("Neispravan broj, pokusajte ponovo.")
        except ValueError:
            print("Neispravan unos, morate unjeti broj!")
    
    #Kalkulacija
    tax = sub_total * 0.10 
    total = sub_total + tax

    offer_number = len(offers) + 1
    
    new_offer = {
        "offer_number": offer_number,
        "customer": selected_customer['name'],
        "date": offer_date,
        "items": selected_products,
        "sub_total": sub_total,
        "tax": tax,
        "total": total
    }
    offers.append(new_offer)
    save_data(OFFERS_FILE, offers)
    
    #Summary
    print("\nNova ponuda je kreirana:")
    print(f"Broj ponude: {new_offer['offer_number']}")
    print(f"Kupac: {new_offer['customer']}")
    print(f"Datum: {new_offer['date']}")
    print("Stavke:")
    for item in new_offer["items"]:
        print(f"  - {item['quantity']}x {item['product_name']} (ID: {item['product_id']}): ${item['item_total']:.2f}")
    print(f"Sub-total: ${new_offer['sub_total']:.2f}")
    print(f"Porez: ${new_offer['tax']:.2f}")
    print(f"Ukupno za platiti: ${new_offer['total']:.2f}")









# TODO: Implementirajte funkciju za upravljanje proizvodima.
def manage_products(products):
    """
    Allows the user to add a new product or modify an existing product.
    """
    # Omogućite korisniku izbor između dodavanja ili izmjene proizvoda
    # Za dodavanje: unesite podatke o proizvodu i dodajte ga u listu products
    # Za izmjenu: selektirajte proizvod i ažurirajte podatke

    while True:
        try:
            print("-" * 60)
            print("Upravljanje proizvodima:")
            print("0. Natrag na glavni izbornik")
            print("1. Dodaj novi proizvod")
            print("2. Izmijeni postojeći proizvod")
            choice = int(input("Odaberite opciju (0, 1 ili 2): "))

            #Dodavanje proizvoda
            if choice == 1:

                new_id = len(products) + 1         
                product_name = input("Unesite naziv proizvoda: ")
                product_description = input("Unesite opis proizvoda: ")
                
                while True:
                    price_input = input("Unesite cijenu proizvoda($): ")
                    try:
                        product_price = float(price_input)
                        break
                    except ValueError:
                        print("Neispravan unos. Molimo unesite cijenu u $.")

                new_product = {
                    "id": new_id,
                    "name": product_name,
                    "description": product_description,
                    "price": product_price
                }
                products.append(new_product)
                print(f"Proizvod '{product_name}' je uspješno dodan.")

                save_data(PRODUCTS_FILE, products)
                exit
            
            #Modifikacija proizvoda
            elif choice == 2:
                print("Odaberite proizvod:")
                for index, product in enumerate(products, start = 1):
                    print(f"{index}. {product['name']} - ${product['price']}")
                while True:
                    try:
                        prod_choice = int(input("Unesite broj proizvoda: "))
                        if 1 <= prod_choice <= len(products):
                            product_to_modify = products[prod_choice - 1]
                            print(f"Odabrani proizvod: {product_to_modify['name']}")
                            break
                        else:
                            print("Neispravan broj")
                    except ValueError:
                        print("Neispravan unos, ocekivan broj")
                
                new_name = input(f"Unesite novi naziv (ostavite prazno za '{product_to_modify['name']}'): ")
                if new_name.strip():
                    product_to_modify['name'] = new_name
                
                new_description = input(f"Unesite novi opis (ostavite prazno za '{product_to_modify['description']}'): ")
                if new_description.strip():
                    product_to_modify['description'] = new_description
                
                new_price_input = input(f"Unesite novu cijenu (ostavite prazno za '{product_to_modify['price']}'): ")
                if new_price_input.strip():
                    try:
                        new_price = float(new_price_input)
                        product_to_modify['price'] = new_price
                    except ValueError:
                        print("Neispravan unos za cijenu. Cijena ostaje nepromijenjena.")
                
                print("Proizvod je uspješno ažuriran.")
                save_data(PRODUCTS_FILE, products)
            
            elif choice == 0:
                return
            
            else:
                print("Nepostojeća opcija.")
        except ValueError:
            print("Neispravan unos.(1/2)")










# TODO: Implementirajte funkciju za upravljanje kupcima.
def manage_customers(customers):
    """
    Allows the user to add a new customer or view all customers.
    """
    # Za dodavanje: omogući unos imena kupca, emaila i unos VAT ID-a
    # Za pregled: prikaži listu svih kupaca
    while True:
        try:
            print("-" * 60)
            print("Upravljanje kupcima:")
            print("0. Natrag na glavni izbornik")
            print("1. Dodaj novog kupca")
            print("2. Prikaži sve kupce")
            choice = int(input("Odaberite opciju (0, 1 ili 2): "))
            
            if choice == 1:
                print("Odabrali ste opciju za dodavanje novog kupca.")
                customer_name = input("Unesite ime kupca: ")
                customer_email = input("Unesite email kupca: ")
                vat_id = input("Unesite VAT ID kupca: ")
                new_customer = {
                    "name": customer_name,
                    "email": customer_email,
                    "vat_id": vat_id
                }
                customers.append(new_customer)
                print(f"Kupac '{customer_name}' je uspješno dodan.")
                save_data(CUSTOMERS_FILE, customers)
            
            elif choice == 2:
                print("Popis kupaca:")
                for index, customer in enumerate(customers, start=1):
                    print(f"{index}. {customer['name']} - {customer['email']} - VAT ID: {customer['vat_id']}")
            
            elif choice == 0:
                return
            
            else:
                print("Nepostojeća opcija. Molimo pokušajte ponovo.")
        except ValueError:
            print("Neispravan unos. Molimo unesite broj (0, 1 ili 2).")






# TODO: Implementirajte funkciju za prikaz ponuda.
def display_offers(offers):
    """
    Display all offers, offers for a selected month, or a single offer by ID.
    """
    # Omogućite izbor pregleda: sve ponude, po mjesecu ili pojedinačna ponuda
    # Prikaz relevantnih ponuda na temelju izbora
    while True:
        try:
            print("-" * 60)
            print("Prikaz ponuda:")
            print("0. Natrag na glavni izbornik")
            print("1. Prikaži sve ponude")
            print("2. Prikaži ponude po mjesecu")
            print("3. Prikaži pojedinačnu ponudu (po ID-u)")
            choice = int(input("Odaberite opciju (0, 1, 2 ili 3): "))
            
            if choice == 0:
                return
            elif choice == 1:
                
                for offer in offers:
                    print_offer(offer)
                break
            elif choice == 2:
                month = input("Unesite mjesec za koji želite prikaz (YYYY-MM): ")
                filtered_offers = [offer for offer in offers if offer['date'].startswith(month)]
                if not filtered_offers:
                    print("Nema ponuda za taj mjesec.")
                else:
                    for offer in filtered_offers:
                        print_offer(offer)
                break
            elif choice == 3:
                try:
                    offer_id = int(input("Unesite ID ponude: "))
                except ValueError:
                    print("Neispravan unos. ID mora biti broj.")
                    continue
                found_offer = None
                for offer in offers:
                    if offer['offer_number'] == offer_id:
                        found_offer = offer
                        break
                if found_offer:
                    print_offer(found_offer)
                else:
                    print("Nije pronađena ponuda s tim ID-om.")
                break
            else:
                print("Nepostojeća opcija. Molimo pokušajte ponovo.")
        except ValueError:
            print("Neispravan unos. Molimo unesite broj (0, 1, 2 ili 3).")






# Pomoćna funkcija za prikaz jedne ponude
def print_offer(offer):
    """Display details of a single offer."""
    #ovdje je bio problem, maknuo sam offer['name'] kod kupca jer je izazivao problem kod prikazivanja u display_offers funkciji
    #TypeError: string indices must be integers, not 'str'
    print(f"Ponuda br: {offer['offer_number']}, Kupac: {offer['customer']}, Datum ponude: {offer['date']}")
    print("Stavke:")
    for item in offer["items"]:
        print(f"  - {item['product_name']} (ID: {item['product_id']}): {item['description']}")
        print(f"    Kolicina: {item['quantity']}, Cijena: ${item['price']}, Ukupno: ${item['item_total']}")
    print(f"Ukupno: ${offer['sub_total']}, Porez: ${offer['tax']}, Ukupno za platiti: ${offer['total']}")


def main():
    # Učitavanje podataka iz JSON datoteka
    offers = load_data(OFFERS_FILE)
    products = load_data(PRODUCTS_FILE)
    customers = load_data(CUSTOMERS_FILE)

    while True:
        print("\nOffers Calculator izbornik:")
        print("1. Kreiraj novu ponudu")
        print("2. Upravljanje proizvodima")
        print("3. Upravljanje korisnicima")
        print("4. Prikaz ponuda")
        print("5. Izlaz")
        choice = input("Odabrana opcija: ")

        if choice == "1":
            create_new_offer(offers, products, customers)
        elif choice == "2":
            manage_products(products)
        elif choice == "3":
            manage_customers(customers)
        elif choice == "4":
            display_offers(offers)
        elif choice == "5":
            # Pohrana podataka prilikom izlaza
            save_data(OFFERS_FILE, offers)
            save_data(PRODUCTS_FILE, products)
            save_data(CUSTOMERS_FILE, customers)
            break
        else:
            print("Krivi izbor. Pokusajte ponovno.")


if __name__ == "__main__":
    main()
  
