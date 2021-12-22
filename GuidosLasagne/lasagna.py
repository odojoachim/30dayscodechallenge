
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(n):
    """Return expected bake time.
        This function takes a number representing elapsed time and
        calculates remaining time that the lasagne should be in the oven"""
    return EXPECTED_BAKE_TIME - n


def preparation_time_in_minutes(m):
    """Return total preparation time for lasagna layers.
        This function takes number of layers you want to add to the lasagna
        and returns how many minutes you would spend making them."""
    return m* PREPARATION_TIME


def elapsed_time_in_minutes(m, n):
    """
        Return elapsed cooking time.
        This function takes two numbers representing the number of layers & the time already spent
        baking and calculates the total elapsed minutes spent cooking the lasagna.
        """
    return preparation_time_in_minutes(m) + n


