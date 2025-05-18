# English language file
#     Written by: Charles J McDonald

# Choose language
language_menu_string = """
Please choose a language:
Choisir une langue:

1. English
2. le français
"""
language_choice_string = "Choose a language: (1/2) "
choose_language_error_string = "Please choose a valid language."
your_language_choice_string = "You have chosen English."

# Choose a currency USD or CAN
currency_menu_string = """
Please choose a currency:
1. USD
2. CAN
"""
choose_currency_string = "Choose a currency: (1/2) "
choose_currency_error_string = "Please choose a valid currency."

# Gather new customer information
vehicle_information_string = "New customer information:"
vehicle_owner_string = "Name of the vehicle owner: "
vehicle_year_string = "Year of the vehicle: "
vehicle_make_string = "Make of the vehicle: "
vehicle_model_string = "Model of the vehicle: "

# Select services
service_menu_string = """
Please choose from the following services:
    1. Oil change and Tyre rotation
    2. Brake Pads and Front-End Alignment
    3. Broken Glass Repair
    4. Dent Removal
"""
choose_service_string = "Choose a service: (1/2/3/4) "
service_oil_change_string = "Oil change and Tire rotation"
service_brake_pads_string = "Brake Pads and Front-End Alightment"
service_broken_glass_string = "Broken Glass Repair"
service_dent_removal_string = "Dent Removal"
service_tyre_type_string = "Enter the type of tyre: (std/4WD/truck) "
window_size_string = "Enter the size of the window: (S/L) "
dent_size_string = "Enter the size of the dent: (S/L) "
tyre_type_error_string = "Please enter a valid tyre type."
glass_size_error_string = "Please enter a valid glass size."
dent_size_error_string = "Please enter a valid dent size."

# Labour cost
service_labour_cost_string = "Enter the cost of labour: "

# Invoice template and tax labels
tax_labels = {
    "USD": "Sales Tax",
    "CAN": "VAT"
}

invoice_template = """
WACTC Automotive Services               INVOICE
400 Alysworth Ave
Woonsocket, RI 02895

{customer_name}
{customer_year} {customer_make} {customer_model}

Service Type: {service_type}
Subtotal: {subtotal:.2f} {currency} including labour
{tax_label} ({tax_percentage}%): {tax_amount:.2f} {currency}
Total Cost: {total_cost:.2f} {currency}
"""

# Another invoice?
another_invoice_string = "Would you like to create another invoice? (y/n) "