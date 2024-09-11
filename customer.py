class Customer:
    def __init__(self, name):
        self.name = name  # Use property setter for validation

    @property
    def name(self):
        #Get the customer's name.
        return self._name

    @name.setter
    def name(self, value):
        # Set the customer's name with validation.
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = value

    def __repr__(self):
        return f"Customer(name={self.name!r})"
