def buy_items(funds, items):
    forex = {
        'USD': 1,
        'EUR': 1.1,
        'GBP': 1.25,
        'JPY': 0.007,
        'CAD': 0.75
    }
    conv_funds = float(funds[0]) * forex[funds[1]]
    items.sort(key=lambda item: float(item[0]) * forex[item[1]])
    count = 0

    for item in items:
        cost = float(item[0]) * forex[item[1]]
        if conv_funds >= cost: 
            print(conv_funds, item, cost)
            conv_funds -= cost
            count += 1
        else:
            break


    return "Buy them all!" if count == len(items) else f"Buy the first {count} items."