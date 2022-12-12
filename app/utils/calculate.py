def calc(*users):
    amount = 0
    for user_collection in users:
        amount += len(user_collection)
    return amount
