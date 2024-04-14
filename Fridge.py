import datetime
from decimal import Decimal

goods = {
    'Хлеб': [
        {'amount': Decimal('1'), 'expiration_date': None},
        {'amount': Decimal('1'), 'expiration_date': datetime.date(2023, 12, 9)}
    ],
    'Яйца': [
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 12, 12)},
        {'amount': Decimal('3'), 'expiration_date': datetime.date(2023, 12, 11)}
    ],
    'Вода': [{'amount': Decimal('100'), 'expiration_date': None}]
}

DATE_FORMAT = '%Y-%m-%d'

def add(items, title, amount, expiration_date=None):
     if expiration_date != None:
        expiration_date = datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()
     if title in items:
         items[title].append({'amount': amount, 'expiration_date': expiration_date})
     else:
         items[title] = [{'amount': amount, 'expiration_date': expiration_date}] 
        
def add_by_note(items, note):
    parts = str.split(note, ' ')  
    if len(str.split(parts[-1], '-')) == 3:
        expiration_date = (parts[-1])
        good_amount = Decimal (parts[-2])
        title = ' '.join(parts[:len(parts)-2])
    else:
        good_amount = Decimal (parts[-1])
        title = ' '.join(parts[:len(parts)-1])
        expiration_date = None
    add(items, title, good_amount, expiration_date=expiration_date)
        
def find(items, needle):
    result = []
    for title in items:
        if needle.lower() in title.lower() or needle.lower() == title.lower():
            result.append(title)
        else:
            continue
    return result

def amount(items, needle):
    product_amount = Decimal('0')
    for title in find(items, needle):
        for parts in items[title]:
            product_amount += parts['amount']
    return product_amount

def expire(items, in_advance_days=0):
    result = []
    today = datetime.date(2023, 12, 10)
    for title in items:
        amount = 0
        for parts in items[title]:
            expiration_date = (parts['expiration_date'])
            if expiration_date and (
                today + datetime.timedelta(days=in_advance_days)) >= expiration_date:
                amount += (parts['amount'])
        if amount > 0:
                result.append((title, amount))
    return result
    