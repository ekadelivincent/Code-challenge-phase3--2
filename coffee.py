class Coffee:
    all_coffees = []  # Track all coffee instances

    def __init__(self, name, price):
        self._name = None  # Initialize to None for validation in setter
        self.price = price
        self.name = name  # Use property setter for validation

    @property
    def name(self):
        """Get the coffee's name."""
        return self._name

    @name.setter
    def name(self, value):
        #Set the coffee's name with validation. It should not be changeable after initialization.
        if hasattr(self, '_name') and self._name is not None:
            raise AttributeError("Cannot change coffee name after it is set.")
        if not isinstance(value, str) or len(value) < 3:
            raise ValueError("Coffee name must be a string with at least 3 characters.")
        self._name = value
        Coffee.all_coffees.append(self)

    @classmethod
    def display_menu(cls):
        """Display a menu of all available coffee and their prices."""
        menu = "\n".join(f"{coffee.name}: ${coffee.price:.2f}" for coffee in cls.all_coffees)
        return menu or "No coffee available."

    def __repr__(self):
        return f"Coffee(name={self.name!r}, price={self.price:.2f})"
