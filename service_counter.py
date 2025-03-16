"""
        package: service_counter.py
         author: Charles J McDonald «cmcdonald@woonsocketschools.com»
   date written: 2025.03.12
    description: Prepare an invoice for an automotive service writer.
"""

# Default language is English
import lang_en as lang

USD_EXCHANGE_RATE = 1.00
CAN_EXCHANGE_RATE = 1.44

def print_english_language_invoice():
    """Prints the english language invoice using global params.
    """
    print(f"""
    WACTC Automotive Services               INVOICE
    400 Alysworth Ave
    Woonsocket, RI 02895
    
    {customer_name}
    {customer_year} {customer_make} {customer_model}
    
    Service Type: {service_type}
    Service Cost: {service_cost:.2f} {currency} including labour""")

def print_french_language_invoice():
    """Prints the french language invoice using global params.
    """
    print(f"""
    WACTC Automotive Services               FACTURE
    400 Alysworth Ave
    Woonsocket, RI 02895

    {customer_name}
    {customer_year} {customer_make} {customer_model}

    Type de service: {service_type}
    Coût du service: {service_cost:.2f} {currency} y compris le travail""")

# Choose language
is_choosing_a_language = True
while is_choosing_a_language:
    print(lang.language_menu_string)
    language_choice = input(lang.language_choice_string)
    if language_choice == "1":
        import lang_en as lang
        is_choosing_a_language = False
    elif language_choice == "2":
        import lang_fr as lang
        is_choosing_a_language = False
    else:
        print(lang.choose_language_error_string)

# Test line to confirm language choice works
# print(lang.language_choice_string)

# Choose a currancy USD or CAN
is_choosing_a_currency = True
while is_choosing_a_currency:
    print(lang.currency_menu_string)
    currency_choice = input(lang.choose_currency_string)
    if currency_choice == "1":
        currency = "USD"
        exchange_rate = USD_EXCHANGE_RATE
        is_choosing_a_currency = False
    elif currency_choice == "2":
        currency = "CAN"
        exchange_rate = CAN_EXCHANGE_RATE
        is_choosing_a_currency = False
    else:
        print(lang.choose_currency_error_string)

# Initial program setup complete, program loop begins here
is_creating_invoices = True
while is_creating_invoices:
    service_cost = 0.00     # initialize service total cost

# Gather new customer information
    print(lang.vehicle_information_string)
    customer_name = input(lang.vehicle_owner_string)
    customer_year = input(lang.vehicle_year_string)
    customer_make = input(lang.vehicle_make_string)
    customer_model = input(lang.vehicle_model_string)

# Select services
    is_choosing_a_service = True
    while is_choosing_a_service:
        print(lang.service_menu_string)
        service_choice = input(lang.choose_service_string)
        if service_choice == "1":
            service_type = lang.service_oil_change_string
            service_cost += (79.99 * exchange_rate)
            is_choosing_a_service_tyre_type = True
            while is_choosing_a_service_tyre_type:
                service_tyre_type = input(lang.service_tyre_type_string).lower()
                if service_tyre_type == "std":
                    service_cost += (30.00 * exchange_rate)
                    is_choosing_a_service_tyre_type = False
                elif service_tyre_type in ("4wd", "truck"):
                    service_cost += (45.00 * exchange_rate)
                    is_choosing_a_service_tyre_type = False
                else:
                    print(lang.tyre_type_error_string)
            is_choosing_a_service = False
        elif service_choice == "2":
            service_type = lang.service_brake_pads_string
            service_cost += (120.00 * exchange_rate)
            is_choosing_a_service = False
        elif service_choice == "3":
            service_type = lang.service_broken_glass_string
            is_choosing_a_glass_size = True
            while is_choosing_a_glass_size:
                window_size = input(lang.window_size_string).lower()
                if window_size == "s":
                    service_cost += (39.99 * exchange_rate)
                    is_choosing_a_glass_size = False
                elif window_size == "l":
                    service_cost += (69.99 * exchange_rate)
                    is_choosing_a_glass_size = False
                else:
                    print(lang.glass_size_error_string)
            is_choosing_a_service = False
        elif service_choice == "4":
            service_type = lang.service_dent_removal_string
            is_choosing_a_dent_size = True
            while is_choosing_a_dent_size:
                dent_size = input(lang.dent_size_string).lower()
                if dent_size == "s":
                    service_cost += (5.00 * exchange_rate)
                    is_choosing_a_dent_size = False
                elif dent_size == "l":
                    service_cost += (15.00 * exchange_rate)
                    is_choosing_a_dent_size = False
                else:
                    print(lang.dent_size_error_string)
            is_choosing_a_service = False
    # End of while loop (choosing_a_service)

    # Add labour fee
    service_labour_cost = input(lang.service_labour_cost_string)
    service_cost += float(service_labour_cost)

    # Print invoice
    if language_choice == "1":
        print_english_language_invoice()
    else:
        print_french_language_invoice()

    # Another invoice?
    another_invoice = input(lang.another_invoice_string).lower()
    if another_invoice != "y":
        is_creating_invoices = False
# End of while loop (is_creating_invoices)
