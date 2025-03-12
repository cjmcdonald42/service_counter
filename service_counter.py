"""
        package: service_counter.py
         author: Charles J McDonald «cmcdonald@woonsocketschools.com»
   date written: 2025.03.12
    description: Write an invoice for an automotive service writer.
"""

# Default language is English
import lang_en as lang

# Choose language
choosing_a_language = True
while choosing_a_language:
    print(lang.language_menu)
    language_choice = input(lang.choose_language)
    if language_choice == "1":
        import lanf_en as lang
    elif language_choice == "2":
        import lanf_fr as lang
    else:
        print(lang.choose_language_error)


# Choose currancy

# Gather new customer information

# Select services

# Calculate total

# Print invoice
