car={
    "suzuki":2015,
    "tata":1997,
    "kia":2000,
    "mahindra":1998


}

oldbrand = None
oldname=""
for car,year in car.items():
    if year is None or year < oldbrand:
        oldbrand = year
        oldname=car

print("oldest car brand:",oldname)
print("year:",oldbrand)        