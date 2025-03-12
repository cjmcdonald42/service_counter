"""
        package: service_counter.py
         author: Charles J McDonald «cmcdonald@woonsocketschools.com»
   date written: 2025.03.12
    description: Prepare an invoice for an automotive service writer.
"""

# Default language is English
import lang_en as lang

# Choose language
choosing_a_language = True
while choosing_a_language:
    print(lang.language_menu)
    language_choice = input(lang.choose_language)
    if language_choice == "1":
        import lang_en as lang
        choosing_a_language = False
    elif language_choice == "2":
        import lang_fr as lang
        choosing_a_language = False
    else:
        print(lang.choose_language_error)

#TODO test line and language string - remove from final project
print(lang.language_choice)

# Choose a currancy USD or CAN
choosing_a_currency = True
while choosing_a_currency:
    print(lang.currency_menu)
    currency_choice = input(lang.choose_currency)
    if currency_choice == "1":
        currency = "USD"
        choosing_a_currency = False
    elif currency_choice == "2":
        currency = "CAN"
        choosing_a_currency = False
    else:
        print(lang.choose_currency_error)

# Initial program setup complete, program loop begins here
is_creating_invoices = True
while is_creating_invoices:
    service_cost = 0.00     # initialize service total cost

# Gather new customer information
    print(lang.vehicle_information)
    customer_name = input(lang.vehicle_owner)
    customer_year = input(lang.vehicle_year)
    customer_make = input(lang.vehicle_make)
    customer_model = input(lang.vehicle_model)

# Select services

    choosing_a_service = True
    while choosing_a_service:
        print(lang.service_menu)
        service_choice = input(lang.choose_service)
        if service_choice == "1":
            service_type = lang.service_oil_change
            service_cost += 79.99
            service_tyre_type = input(lang.tyre_type).lower()
            if service_tyre_type == "std":
                service_cost += 30.00
            elif service_tyre_type == "4wd" or service_tyre_type == "truck":
                service_cost += 45.00
            choosing_a_service = False
        elif service_choice == "2":
            service_type = lang.service_brake_pads
            service_cost += 120.00
            choosing_a_service = False
        elif service_choice == "3":
            service_type = lang.service_broken_glass
            window_size = input(lang.window_size_string).lower()
            if window_size == "s":
                service_cost += 39.99
            elif window_size == "l":
                service_cost += 69.99
            choosing_a_service = False
        elif service_choice == "4":
            service_type = lang.service_dent_removal
            dent_size = input(lang.dent_size_string).lower()
            if dent_size == "s":
                service_cost += 5.00
            else:
                service_cost += 15.00
            choosing_a_service = False
    # End of while loop (choosing_a_service)

    # Add labour fee
    service_labour_cost = input(lang.service_labour_cost_string)
    service_cost += float(service_labour_cost)

    # TODO: Calculate Tax or VAT?

    # Print invoice
    print(lang.invoice_string)

    # Another invoice?
    another_invoice = input(lang.another_invoice_string).lower()
    if another_invoice != "y":
        is_creating_invoices = False
# End of while loop (is_creating_invoices)
