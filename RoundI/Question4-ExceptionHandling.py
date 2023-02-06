def main():
    qty = None
    cost = None

    try:
        qty = fetch_quantity()
    except Exception as e:
        print(e)
        return

    try:
        cost = fetch_cost()
    except Exception as e:
        print("Exception in fetch_cost(): ", e)

    try:
        cost_per_quantity = cost / qty
    except Exception as e:
        print("Exception in cost/qty calculation: ", e)
def fetch_quantity():
    """
    Returns a number, any number
    """
    ...
    return ...
def fetch_cost():
    """
    Returns a number, any number
    """
    ...
    return ...
def compute_cost_per_quantity():
    qty = fetch_quantity()
    cost = fetch_cost()
    cost_per_quantity = cost/qty
    return cost_per_quantity
    cost_per_quantity = compute_cost_per_quantity()
    a = 1 + 2 + cost_per_quantity
    b = 4 + 5
    print(a+b)
