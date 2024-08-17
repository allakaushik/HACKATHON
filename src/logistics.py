def select_delivery_option(option):
    options = {1: "Pickup at mall", 2: "Home delivery"}
    return options.get(option, "Invalid option")
